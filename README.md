# EduTech Platform - Sistema de Gerenciamento de Cursos Online

Sistema de gerenciamento de plataforma de cursos online desenvolvido com PostgreSQL e Python, focado em modelagem de banco de dados relacional e scripts auxiliares para geração e processamento de dados.

## 🚀 Tecnologias

- **PostgreSQL 15**: Banco de dados relacional
- **Python 3.10+**: Scripts de automação e processamento
- **Docker & Docker Compose**: Containerização
- **Faker**: Geração de dados fictícios
- **Pandas**: Processamento de dados

## 📁 Estrutura do Projeto

```
edutech_m1/
├── edutech/               # Package principal
│   ├── sql/              # Scripts SQL
│   │   ├── schema.sql    # DDL - Criação de tabelas
│   │   ├── dados.sql     # DML - Inserção de dados
│   │   └── consultas.sql # Consultas e relatórios
│   ├── scripts/          # Scripts Python
│   │   ├── __init__.py
│   │   ├── gerador_dados.py   # Geração de dados fictícios
│   │   ├── validador_csv.py   # Validação de CSVs
│   │   ├── processador_relatorios.py  # Processamento de relatórios
│   │   └── utils.py           # Funções auxiliares
│   └── data/             # CSVs gerados
├── docs/                 # Documentação
├── docker-compose.yml    # Configuração Docker
├── Makefile             # Comandos de automação
├── requirements.txt     # Dependências Python
└── README.md
```

## 🔧 Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.10 ou superior
- Make (opcional, mas recomendado)

## ⚙️ Configuração Inicial

### 1. Clone o repositório

```bash
git clone <repository-url>
cd edutech_m1
```

### 2. Configure as variáveis de ambiente (opcional)

```bash
cp .env.example .env
# Edite o arquivo .env se necessário
```

### 3. Instale as dependências Python

```bash
pip install -r requirements.txt
```

## 📊 Modelo de Dados

O sistema possui 9 tabelas principais:

- **alunos**: Dados dos estudantes
- **instrutores**: Dados dos professores
- **categorias**: Categorias de cursos
- **cursos**: Informações dos cursos
- **modulos**: Módulos dos cursos
- **aulas**: Aulas individuais
- **matriculas**: Matrículas de alunos em cursos
- **progresso_aulas**: Progresso dos alunos nas aulas
- **avaliacoes**: Avaliações dos cursos pelos alunos

Veja o diagrama ER completo em `docs/diagrama_er.png`

## 🤝 Contribuindo

Este é um projeto acadêmico. Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto é desenvolvido para fins educacionais.

## ✨ Autor

Desenvolvido como parte do projeto M1 & M2 - Sistema de Gerenciamento de Cursos Online (EduTech)