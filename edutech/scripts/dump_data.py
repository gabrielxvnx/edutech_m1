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
        dbname=os.getenv('DB_NAME', 'edutech_db'),
        user=os.getenv('DB_USER', 'edutech_user'),
        password=os.getenv('DB_PASSWORD', 'edutech_pass')
    )
    return conn

def dump_tabela(conn, tabela_nome: str, df: pd.DataFrame):
    """Insere DF na tabela via copy_from (rápido pra bulk)."""
    cur = conn.cursor()
    
    # Truncate opcional (comente se não quiser limpar)
    cur.execute(f"TRUNCATE TABLE {tabela_nome} CASCADE;")
    
    # Prepara colunas
    cols = ', '.join(df.columns)
    
    # Usa StringIO pra copy_from
    from io import StringIO
    output = StringIO()
    df.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    
    cur.copy_from(output, tabela_nome, null="\\N", columns=df.columns.tolist())
    conn.commit()
    cur.close()
    print(f"✅ Dumped {len(df)} rows para {tabela_nome}")