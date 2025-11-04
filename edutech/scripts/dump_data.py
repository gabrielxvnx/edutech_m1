import os
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
from pathlib import Path

# Ordem de insert (respeita dependências FK)
TABELAS_ORDEM = [
    'categorias',
    'instrutores',
    'alunos',
    'cursos',
    'modulos',
    'aulas',
    'matriculas',
    'progresso_aulas',
    'avaliacoes'
]

def conectar_banco():
    """Conecta ao PostgreSQL. Ajuste creds."""
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        dbname=os.getenv('DB_NAME', 'edutech'),
        user=os.getenv('DB_USER', 'edutech_user'),
        password=os.getenv('DB_PASSWORD', 'edutech_pass')
    )
    return conn

def dump_tabela(conn, tabela_nome: str, df: pd.DataFrame):
    """Insere DF na tabela via COPY."""
    cur = conn.cursor()
    
    # Prepara colunas
    cols = ', '.join(f'"{col}"' for col in df.columns)
    
    # Usa StringIO para COPY
    from io import StringIO
    output = StringIO()
    df.to_csv(output, sep=',', header=False, index=False, na_rep='\\N')
    output.seek(0)
    
    # Usa COPY com formato CSV que é mais robusto
    cur.copy_expert(
        f"""
        COPY {tabela_nome} ({cols})
        FROM STDIN WITH (
            FORMAT csv,
            NULL '\\N'
        )
        """,
        output
    )
    conn.commit()
    cur.close()
    print(f"Dumped {len(df)} rows para {tabela_nome}")