from pathlib import Path
import pandas as pd
from csv_validator import validar_csv, validar_fks
from dump_data import conectar_banco, dump_tabela, TABELAS_ORDEM

# Mapeamento de colunas de data para cada tabela
COLUNAS_DATA = {
    'alunos': ['data_nascimento', 'data_cadastro'],
    'instrutores': ['data_cadastro'],
    'cursos': ['data_criacao'],
    'matriculas': ['data_matricula', 'data_conclusao'],
    'progresso_aulas': ['data_conclusao'],
    'avaliacoes': ['data_avaliacao']
}

def carregar_dfs(data_dir: Path) -> dict:
    """Carrega todos CSVs em um dict {tabela: df}."""
    dfs = {}
    for tabela in TABELAS_ORDEM:
        csv_path = data_dir / f"{tabela}.csv"
        if csv_path.exists():
            # Pega apenas as colunas de data específicas para esta tabela
            parse_dates = COLUNAS_DATA.get(tabela, [])
            # Remove colunas que não existem no arquivo
            df = pd.read_csv(csv_path)
            colunas_existentes = [col for col in parse_dates if col in df.columns]
            
            if colunas_existentes:
                df = pd.read_csv(csv_path, parse_dates=colunas_existentes)
            else:
                df = pd.read_csv(csv_path)
                
            dfs[tabela] = df
            print(f" Carregado {tabela}: {len(df)} rows")
        else:
            print(f" CSV não encontrado: {csv_path}")
    return dfs

def main():
    # Diretório de dados
    data_dir = Path(__file__).parent.parent / 'data'
    if not data_dir.exists():
        print(f"Diretório não encontrado: {data_dir}")
        return

    # Carrega DFs
    dfs = carregar_dfs(data_dir)
    if not dfs:
        print("Nenhum CSV encontrado. Gere dados primeiro.")
        return

    # Validação
    print("\n Iniciando validação...")
    resultados = {}
    for tabela, df in dfs.items():
        sucesso = validar_csv(df, tabela)
        resultados[tabela] = sucesso

    # Checa FKs
    if not validar_fks(dfs):
        print(" Validação de FKs falhou.")
        return

    if not all(resultados.values()):
        print(" Validação falhou. Corrija CSVs.")
        return

    print("Todos CSVs válidos!")

    # Dump
    print("\n Iniciando dump para o banco...")
    conn = conectar_banco()
    try:
        for tabela in TABELAS_ORDEM:
            if tabela in dfs:
                dump_tabela(conn, tabela, dfs[tabela])
        print(" Dump completo!")
    except Exception as e:
        print(f" Erro no dump: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    main()