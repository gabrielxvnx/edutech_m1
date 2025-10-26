from faker import Faker
from typing import List, Dict
import csv
from datetime import datetime, timedelta
import random


class GeradorDados:
    """Gera dados fictícios realistas"""
    
    def __init__(self, locale: str = 'pt_BR'):
        self.fake = Faker(locale)
        self.categorias = []
        self.instrutores = []
        self.alunos = []
        self.cursos = []
        self.modulos = []
        self.aulas = []
        self.matriculas = []
        
    # def gerar_categorias(self, quantidade: int = 5) -> List[Dict]:
    # def gerar_instrutores(self, quantidade: int = 10) -> List[Dict]
    # def gerar_alunos(self, quantidade: int = 30) -> List[Dict]
    # def gerar_cursos(self, quantidade: int = 20) -> List[Dict]
    # def gerar_modulos_e_aulas(self, curso_id: int, num_modulos: int, num_aulas_por_modulo: int) -> tuple
    # def gerar_matriculas(self, quantidade: int = 80) -> List[Dict]
    # def gerar_progresso_aulas(self) -> List[Dict]
    # def gerar_avaliacoes(self) -> List[Dict]
    def exportar_para_csv(self, diretorio: str = 'data/'):
        """Exporta os dados gerados para arquivos CSV"""
        tabelas = {
            'categorias': self.categorias,
            'instrutores': self.instrutores,
            'alunos': self.alunos,
            'cursos': self.cursos,
            'modulos': self.modulos,
            'aulas': self.aulas,
            'matriculas': self.matriculas,
            # 'progresso_aulas': self.progresso_aulas,
            # 'avaliacoes': self.avaliacoes
        }
        
        for nome_tabela, dados in tabelas.items():
            if dados:
                with open(f'{diretorio}{nome_tabela}.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
                    escritor = csv.DictWriter(arquivo_csv, fieldnames=dados[0].keys())
                    escritor.writeheader()
                    escritor.writerows(dados)
