from faker import Faker
from typing import List, Dict
import csv
from datetime import datetime, timedelta
import random
import os


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
        
        # Constantes para requisitos mínimos
        self.MIN_CATEGORIAS = 5
        self.MIN_INSTRUTORES = 10
        self.MIN_CURSOS = 20
        self.MIN_AULAS_TOTAL = 50  # Distribuídas entre os cursos
        self.MIN_ALUNOS = 30
        self.MIN_MATRICULAS = 80
        
    def gerar_categorias(self, quantidade: int = 5) -> List[Dict]:
        """Gera categorias de cursos"""
        categorias = []
        areas = ['Programação', 'Data Science', 'Design', 'Marketing Digital', 'Negócios',
                'Desenvolvimento Pessoal', 'Idiomas', 'Música', 'Fotografia', 'Finanças']
        
        for i in range(1, quantidade + 1):
            categoria = {
                'id': i,
                'nome': areas[i-1] if i <= len(areas) else self.fake.word().capitalize(),
                'descricao': self.fake.text(max_nb_chars=200)
            }
            categorias.append(categoria)
        self.categorias = categorias
        return categorias

    def gerar_instrutores(self, quantidade: int = None) -> List[Dict]:
        """Gera dados de instrutores"""
        if quantidade is None:
            quantidade = self.MIN_INSTRUTORES

        instrutores = []
        especialidades = ['Desenvolvimento Web', 'Data Science', 'Machine Learning', 
                         'DevOps', 'Mobile', 'Cloud Computing', 'Segurança', 
                         'Frontend', 'Backend', 'Fullstack']
        
        for i in range(1, quantidade + 1):
            instrutor = {
                'id': i,
                'nome': self.fake.name(),
                'email': self.fake.email(),
                'biografia': self.fake.text(max_nb_chars=300),
                'especialidade': especialidades[i-1] if i <= len(especialidades) else self.fake.job()
            }
            instrutores.append(instrutor)
        self.instrutores = instrutores
        return instrutores

    def gerar_alunos(self, quantidade: int = 30) -> List[Dict]:
        """Gera dados de alunos"""
        alunos = []
        for i in range(1, quantidade + 1):
            aluno = {
                'id': i,
                'nome': self.fake.name(),
                'email': self.fake.email(),
                'data_nascimento': self.fake.date_of_birth(minimum_age=16, maximum_age=70).isoformat(),
                'data_cadastro': self.fake.date_between(start_date='-1y').isoformat()
            }
            alunos.append(aluno)
        self.alunos = alunos
        return alunos

    def gerar_cursos(self, quantidade: int = None) -> List[Dict]:
        """Gera dados de cursos"""
        if quantidade is None:
            quantidade = self.MIN_CURSOS
            
        if not self.categorias or not self.instrutores:
            raise ValueError("Categorias e instrutores devem ser gerados primeiro")
        
        cursos = []
        niveis = ['iniciante', 'intermediario', 'avancado']
        
        for i in range(1, quantidade + 1):
            nivel = random.choice(niveis)
            data_inicio = self.fake.date_between(start_date='+1m', end_date='+3m')
            duracao_meses = random.randint(1, 6)
            data_fim = data_inicio + timedelta(days=30*duracao_meses)
            
            curso = {
                'id': i,
                'titulo': f"{self.fake.catch_phrase()} - {nivel.title()}",
                'descricao': self.fake.text(max_nb_chars=300),
                'data_inicio': data_inicio.isoformat(),
                'data_fim': data_fim.isoformat(),
                'categoria_id': random.choice(self.categorias)['id'],
                'instrutor_id': random.choice(self.instrutores)['id'],
                'carga_horaria': random.randint(20, 120),
                'nivel': nivel,
                'preco': random.choice([0, random.randint(5000, 50000)]) / 100,  # Preços entre R$50-500 ou gratuito
                'data_criacao': datetime.now().isoformat()
            }
            cursos.append(curso)
        self.cursos = cursos
        return cursos

    def gerar_modulos_e_aulas(self, curso_id: int, num_modulos: int = 3, num_aulas_por_modulo: int = None) -> tuple:
        """Gera módulos e aulas para um curso específico"""
        # Calcula número de aulas por módulo para atingir o mínimo total
        if num_aulas_por_modulo is None:
            aulas_por_curso = max(3, self.MIN_AULAS_TOTAL // len(self.cursos))
            num_aulas_por_modulo = aulas_por_curso // num_modulos
            
        modulos_gerados = []
        aulas_geradas = []
        modulo_id_counter = len(self.modulos) + 1
        aula_id_counter = len(self.aulas) + 1
        
        for i in range(num_modulos):
            modulo = {
                'id': modulo_id_counter + i,
                'curso_id': curso_id,
                'titulo': f"Módulo {i+1}: {self.fake.catch_phrase()}",
                'descricao': self.fake.text(max_nb_chars=300),
                'ordem': i + 1
            }
            modulos_gerados.append(modulo)
            
            for j in range(num_aulas_por_modulo):
                duracao = random.randint(10, 45)  # duração em minutos
                aula = {
                    'id': aula_id_counter,
                    'modulo_id': modulo['id'],
                    'titulo': f"Aula {j+1}: {self.fake.catch_phrase()}",
                    'duracao_minutos': duracao,
                    'conteudo': self.fake.text(max_nb_chars=500)
                }
                aulas_geradas.append(aula)
                aula_id_counter += 1
        
        self.modulos.extend(modulos_gerados)
        self.aulas.extend(aulas_geradas)
        return modulos_gerados, aulas_geradas

    def gerar_matriculas(self, quantidade: int = 80) -> List[Dict]:
        """Gera matrículas de alunos em cursos"""
        if not self.alunos or not self.cursos:
            raise ValueError("Alunos e cursos devem ser gerados primeiro")
            
        # Gera todas as possíveis combinações de aluno-curso
        alunos_ids = [aluno['id'] for aluno in self.alunos]
        cursos_ids = [curso['id'] for curso in self.cursos]
        
        # Usa o random_elements do faker para selecionar combinações únicas
        combinacoes = [
            (aluno_id, curso_id) 
            for aluno_id in alunos_ids 
            for curso_id in cursos_ids
        ]
        combinacoes_selecionadas = self.fake.random_elements(
            elements=combinacoes,
            length=min(quantidade, len(combinacoes)),
            unique=True
        )
        
        matriculas = []
        for i, (aluno_id, curso_id) in enumerate(combinacoes_selecionadas, 1):
            data_matricula = self.fake.date_between(start_date='-1y')
            curso = next(c for c in self.cursos if c['id'] == curso_id)
            valor_pago = curso['preco']
            
            # Aplica descontos aleatórios (10%, 15% ou 20%) em alguns casos
            if self.fake.boolean(chance_of_getting_true=30):
                desconto = self.fake.random_element(elements=[0.9, 0.85, 0.8])
                valor_pago = round(valor_pago * desconto, 2)
            
            matricula = {
                'id': i,
                'aluno_id': aluno_id,
                'curso_id': curso_id,
                'data_matricula': data_matricula.isoformat(),
                'status': self.fake.random_element(elements=('ativa', 'concluida', 'cancelada')),
                'data_conclusao': (data_matricula + timedelta(days=self.fake.random_int(30, 180))).isoformat() if self.fake.boolean(chance_of_getting_true=30) else None,
                'valor_pago': valor_pago
            }
            matriculas.append(matricula)
            
        self.matriculas = matriculas
        return matriculas

    def gerar_progresso_aulas(self) -> List[Dict]:
        """Gera registro de progresso dos alunos nas aulas"""
        if not self.matriculas or not self.aulas:
            raise ValueError("Matriculas e aulas devem ser geradas primeiro")
            
        progresso_aulas = []
        progresso_id = 1
        
        for matricula in self.matriculas:
            # Pega todas as aulas do curso
            aulas_curso = [aula for aula in self.aulas 
                         if any(modulo['curso_id'] == matricula['curso_id'] 
                               for modulo in self.modulos if modulo['id'] == aula['modulo_id'])]
            
            # Gera progresso para algumas aulas aleatoriamente
            for aula in aulas_curso:
                if random.random() > 0.3:  # 70% de chance de ter progresso
                    data_inicio = datetime.fromisoformat(matricula['data_matricula'])
                    concluida = random.random() > 0.3  # 70% de chance de estar concluída
                    
                    progresso = {
                        'id': progresso_id,
                        'matricula_id': matricula['id'],
                        'aula_id': aula['id'],
                        'concluida': concluida,
                        'data_conclusao': (data_inicio + timedelta(days=random.randint(1, 30))).isoformat() if concluida else None,
                        'tempo_assistido_minutos': random.randint(0, aula['duracao_minutos'])
                    }
                    progresso_aulas.append(progresso)
                    progresso_id += 1
        
        return progresso_aulas

    def gerar_avaliacoes(self) -> List[Dict]:
        """Gera avaliações dos alunos para os cursos"""
        if not self.matriculas:
            raise ValueError("Matriculas devem ser geradas primeiro")
            
        avaliacoes = []
        avaliacao_id = 1
        
        for matricula in self.matriculas:
            if random.random() > 0.3:  # 70% de chance de ter avaliação
                data_matricula = datetime.fromisoformat(matricula['data_matricula'])
                avaliacao = {
                    'id': avaliacao_id,
                    'matricula_id': matricula['id'],
                    'curso_id': matricula['curso_id'],
                    'nota': random.randint(1, 10),  # Nota de 1 a 10 conforme schema
                    'comentario': self.fake.text(max_nb_chars=300) if random.random() > 0.5 else None,
                    'data_avaliacao': (data_matricula + timedelta(days=random.randint(7, 90))).isoformat()
                }
                avaliacoes.append(avaliacao)
                avaliacao_id += 1
        
        return avaliacoes
    
    def exportar_para_csv(self, diretorio: str = None):
        """Exporta os dados gerados para arquivos CSV"""
        if diretorio is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # /edutech
            diretorio = os.path.join(base_dir, 'data')

        os.makedirs(diretorio, exist_ok=True)
        print(f"Criando arquivos csv em: {os.path.abspath(diretorio)}")

        tabelas = {
            'categorias': self.categorias,
            'instrutores': self.instrutores,
            'alunos': self.alunos,
            'cursos': self.cursos,
            'modulos': self.modulos,
            'aulas': self.aulas,
            'matriculas': self.matriculas,
            'progresso_aulas': self.gerar_progresso_aulas(),
            'avaliacoes': self.gerar_avaliacoes()
        }
        
        for nome_tabela, dados in tabelas.items():
            if dados:
                # Garantir que os IDs são números
                for item in dados:
                    for campo in ['id', 'categoria_id', 'instrutor_id', 'curso_id', 'modulo_id', 'aluno_id', 'matricula_id', 'aula_id']:
                        if campo in item and item[campo] is not None:
                            item[campo] = int(item[campo])
                    
                caminho_arquivo = os.path.join(diretorio, f"{nome_tabela}.csv")
                with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
                    escritor = csv.DictWriter(arquivo_csv, fieldnames=dados[0].keys())
                    escritor.writeheader()
                    escritor.writerows(dados)
                print(f"Arquivo '{caminho_arquivo}' criado com sucesso.")  # Opcional: para debug

if __name__ == "__main__":
    gerador = GeradorDados()
    gerador.gerar_categorias()
    gerador.gerar_instrutores()
    gerador.gerar_alunos()
    gerador.gerar_cursos()
    
    # Gerar módulos e aulas para cada curso
    for curso in gerador.cursos:
        gerador.gerar_modulos_e_aulas(curso_id=curso['id'])
    
    gerador.gerar_matriculas()
    
    # Exportar dados para CSV
    gerador.exportar_para_csv()