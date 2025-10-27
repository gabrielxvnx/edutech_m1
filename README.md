# Sistema de Gerenciamento de Cursos (EduTech)

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge\&logo=postgresql\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)

Este projeto consiste na criação de um sistema de gerenciamento para uma plataforma de cursos online (EduTech). O foco principal é a modelagem de um banco de dados relacional robusto com PostgreSQL, a criação de consultas SQL complexas e o uso de Python como ferramenta auxiliar para geração, validação e carga de dados.

***

## Sumário

* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Funcionalidades](#funcionalidades)
* [Modelo do Banco de Dados](#modelo-do-banco-de-dados)
* [Estrutura de Pastas](#estrutura-de-pastas)
* [Como Executar o Projeto](#como-executar-o-projeto)
* [Exemplos de Consultas SQL](#exemplos-de-consultas-sql)

***

## Tecnologias Utilizadas

* **Banco de Dados:** PostgreSQL
* **Linguagem de Scripting:** Python 3.x
* **Containerização:** Docker / Docker Compose
* **Bibliotecas Python:**
  * `psycopg2-binary`: Driver para conexão com o PostgreSQL.
  * `Faker`: Para geração de dados fictícios.
  * `pandas`: Para manipulação e validação dos dados em formato CSV.

***

## Funcionalidades

### Parte 1: SQL

* **Schema Completo:** Modelagem de 9 tabelas normalizadas para representar alunos, cursos, matrículas, progresso, avaliações, etc.
* **Constraints e Índices:** Uso de `FOREIGN KEY`, `UNIQUE`, `CHECK` e `INDEX` para garantir a integridade dos dados e otimizar o desempenho das consultas.
* **Views:** Criação de views para simplificar a execução de consultas complexas e recorrentes.
* **Consultas Avançadas:** Implementação de mais de 12 consultas SQL para extrair insights de negócio, utilizando `JOINs`, agregações, subconsultas e funções analíticas.

### Parte 2: Python

* **Geração de Dados:** Script (`data_generator.py`) que utiliza a biblioteca Faker para popular o banco de dados com dados fictícios e realistas.
* **Validação de Dados:** Script (`csv_validator.py`) que realiza um conjunto de validações nos arquivos CSV antes da importação, verificando tipos de dados, formatos e integridade referencial.
* **Carga de Dados:** Script principal (`main.py`) que orquestra a validação e a importação eficiente dos dados para o banco de dados PostgreSQL utilizando o comando `COPY`.

***

## Modelo do Banco de Dados

O diagrama Entidade-Relacionamento (ER) abaixo ilustra a estrutura do banco de dados. Para uma explicação detalhada sobre cada tabela, relacionamentos e as decisões de modelagem, consulte a [Documentação do Modelo de Dados](docs/DIAGRAMA_ER.md).

![1.00](docs/drawSQL-image-export-2025-10-26%20\(1\).png)

***

## Estrutura de Pastas

O projeto está organizado da seguinte forma para manter uma clara separação de responsabilidades:

```
edutech_m1/
├── .env.example         # Exemplo de variáveis de ambiente
├── docker-compose.yml   # Arquivo de configuração do Docker para o PostgreSQL
├── requirements.txt     # Dependências Python
├── edutech/
│   ├── data/            # Arquivos CSV com os dados gerados
│   ├── scripts/         # Scripts Python para geração, validação e carga
│   └── sql/
│       ├── init/        # Scripts de inicialização do banco (schema, views)
│       └── queries.sql  # Consultas SQL de negócio
└── docs/
    └── ...              # Documentação e diagrama ER
```

---

## Arquitetura e Fluxo do Projeto

Para entender como os diferentes componentes do projeto (scripts, banco de dados, SQL) se conectam e operam, foi criada uma documentação visual com diagramas. Ela ilustra desde a geração dos dados até a forma como as consultas são abstraídas.

Para mais detalhes, consulte a [Documentação de Arquitetura e Fluxo do Projeto](docs/ARCHITECTURE.md).

***

## Como Executar o Projeto

Siga os passos abaixo para configurar e executar o ambiente de desenvolvimento localmente.

### Pré-requisitos

* [Docker](https://www.docker.com/get-started) e [Docker Compose](https://docs.docker.com/compose/install/) instalados.
* [Python 3.8+](https://www.python.org/downloads/) instalado.

### Passo 1: Iniciar o Banco de Dados

Com o Docker em execução, inicie o container do PostgreSQL em modo `detached` (background).

```Shell
docker-compose up -d
```

O banco de dados estará disponível em `localhost:5432`. As credenciais e o nome do banco são definidos no arquivo `.env` (copie do `.env.example` se necessário).

#### Inicialização Automática do Schema

O serviço do PostgreSQL no `docker-compose.yml` está configurado para inicializar o banco de dados automaticamente. Ele utiliza o seguinte volume:

```yaml
volumes:
  - ./edutech/sql/init:/docker-entrypoint-initdb.d:ro
```

A imagem oficial do `postgres` executa quaisquer scripts `.sql` ou `.sh` localizados no diretório `/docker-entrypoint-initdb.d` na primeira vez que o container é iniciado. Em nosso projeto, isso garante que o `01_schema.sql` e o `03_views.sql` sejam executados em ordem, criando todas as tabelas e views necessárias antes mesmo da inserção dos dados.

### Passo 2: Configurar o Ambiente Python

É altamente recomendável usar um ambiente virtual (`venv`) para isolar as dependências do projeto.

```Shell
# Crie um ambiente virtual
python -m venv .venv

# Ative o ambiente virtual
# No Windows:
.\.venv\Scripts\activate
# No macOS/Linux:
source .venv/bin/activate

# Instale as dependências do projeto
pip install -r requirements.txt
```

### Passo 3: Validar e Popular o Banco de Dados

Os dados já foram gerados e estão na pasta `edutech/data/`. O script principal irá validar esses arquivos e, se estiverem corretos, irá inseri-los no banco de dados.

Execute o script `main.py`:

```Shell
python edutech/scripts/main.py
```

Ao final da execução, o banco de dados estará populado e pronto para ser consultado.

### (Opcional) Gerar Novos Dados

Caso queira gerar um novo conjunto de dados fictícios, você pode executar o script `data_generator.py`. **Atenção:** isso irá sobrescrever os arquivos existentes na pasta `edutech/data/`.

```Shell
python edutech/scripts/data_generator.py
```

***

## Exemplos de Consultas SQL

O arquivo `edutech/sql/queries.sql` contém todas as consultas desenvolvidas. Aqui estão alguns exemplos:

**1. Listar todos os cursos com detalhes da categoria e do instrutor**

```SQL
SELECT curso_id, curso_titulo, categoria_nome, instrutor_nome
FROM vw_cursos_detalhes
ORDER BY categoria_nome, curso_titulo;
```

**2. Calcular o faturamento total por categoria**

```SQL
SELECT categoria_nome, total_cursos, faturamento_total
FROM vw_faturamento_categoria
ORDER BY faturamento_total DESC;
```

**3. Top 5 cursos mais rentáveis**

```SQL
SELECT curso_id, titulo, faturamento_total, media_avaliacoes
FROM vw_cursos_mais_rentaveis
ORDER BY faturamento_total DESC
LIMIT 5;
```

