from datetime import date, datetime
import pandas as pd

def validar_csv(df: pd.DataFrame, tabela: str) -> bool:
    """Validação CSVs com regras não cobertas pelo SQL."""
    erros = []
    
    # Regras por tabela
    regras = {
        'alunos': {
            'email': lambda x: '@' in str(x),
            'data_nascimento': lambda x: isinstance(x, (str, date)) and pd.to_datetime(x) < pd.Timestamp.now()
        },
        'instrutores': {
            'email': lambda x: '@' in str(x)
        },
        'cursos': {
            'data_inicio': lambda x: isinstance(x, (str, date)),
            'data_fim': lambda x: isinstance(x, (str, date)),
            'nivel': lambda x: str(x).lower() in ['iniciante', 'intermediario', 'avancado']
        },
        'matriculas': {
            'status': lambda x: str(x) in ['ativa', 'concluida', 'cancelada']
        }
    }
    
    # Se a tabela tem regras específicas
    if tabela in regras:
        # Valida cada coluna que tem regra
        for coluna, validador in regras[tabela].items():
            if coluna in df.columns:
                invalidos = df[~df[coluna].apply(validador)]
                if not invalidos.empty:
                    erros.append(f"Valores inválidos em {coluna}: linhas {list(invalidos.index + 1)}")
    
    # Validações gerais de datas (data_fim > data_inicio, etc)
    if 'data_fim' in df.columns and 'data_inicio' in df.columns:
        df['data_inicio'] = pd.to_datetime(df['data_inicio'])
        df['data_fim'] = pd.to_datetime(df['data_fim'])
        invalidos = df[df['data_fim'] <= df['data_inicio']]
        if not invalidos.empty:
            erros.append(f"data_fim deve ser posterior a data_inicio: linhas {list(invalidos.index + 1)}")
    
    if erros:
        print(f"\n Erros em {tabela}:")
        for erro in erros:
            print(f"- {erro}")
        return False
        
    print(f"{tabela} OK! ({len(df)} registros)")
    return True

def validar_fks(dfs: dict) -> bool:
    """Valida FKs entre tabelas antes do dump."""
    # Mapeamento de FKs: tabela -> [(coluna, tabela_ref)]
    fks = {
        'cursos': [('categoria_id', 'categorias'), ('instrutor_id', 'instrutores')],
        'modulos': [('curso_id', 'cursos')],
        'aulas': [('modulo_id', 'modulos')],
        'matriculas': [('aluno_id', 'alunos'), ('curso_id', 'cursos')],
        'progresso_aulas': [('matricula_id', 'matriculas'), ('aula_id', 'aulas')],
        'avaliacoes': [('matricula_id', 'matriculas'), ('curso_id', 'cursos')]
    }
    
    erros = []
    for tabela, fk_list in fks.items():
        if tabela not in dfs:
            continue
            
        df = dfs[tabela]
        for coluna, tabela_ref in fk_list:
            if coluna not in df.columns or tabela_ref not in dfs:
                continue
                
            valores = set(df[coluna].dropna())
            valores_ref = set(dfs[tabela_ref]['id'])
            invalidos = valores - valores_ref
            
            if invalidos:
                erros.append(f"{tabela}.{coluna} tem valores inválidos: {invalidos}")
    
    if erros:
        print("\n❌ Erros de FK:")
        for erro in erros:
            print(f"- {erro}")
        return False
    
    return True