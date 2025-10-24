# 

# 

# 

# 

# Mini Projeto

**Sistema de Gerenciamento de Cursos Online (EduTech)**

# Sumário

[**Descrição	2**](#heading)

[**Requisitos	2**](#requisitos)

[**Utilitários	3**](#utilitários)

[Arrays e Objetos em JavaScript](#bancos-de-dados-relacionais-e-postgresql)

[Métodos Funcionais de Arrays](#normalizacao-de-dados)

[Rubrica	3](#rubrica)

#         {#heading}

# Descrição

Como pessoa desenvolvedora back-end, uma das habilidades mais valiosas é dominar a modelagem e consulta de bancos de dados relacionais, além de saber usar Python para auxiliar no processamento e preparação de dados. Esta combinação é a base para o desenvolvimento de APIs REST robustas.

Neste projeto você deve criar um **sistema de gerenciamento de uma plataforma de cursos online (EduTech)** focando fortemente em SQL/PostgreSQL (70% do projeto) e utilizando Python como ferramenta auxiliar (30% do projeto). O sistema deve ter uma modelagem de dados sólida, consultas SQL complexas e scripts Python para geração de dados e validações.

**O foco principal é SQL:** você vai criar um banco de dados completo, normalizado e com consultas avançadas que demonstrem domínio de JOINs, agregações, filtros e subconsultas.

**Python será auxiliar:** você vai criar scripts para gerar dados fictícios realistas (usando bibliotecas como Faker), validar arquivos antes de importação manual no banco, e processar exports para gerar relatórios. Isso prepara o terreno para quando você criar APIs REST no futuro.

Este tipo de estrutura é fundamental no desenvolvimento back-end, onde APIs precisam de bancos bem modelados e a capacidade de processar dados antes de armazená-los ou após consultá-los.

# Requisitos {#requisitos}

**Funcionalidades Obrigatórias:**

**PARTE 1: Modelagem e Consultas SQL (70% do projeto) 🎯**

**1.1 Modelagem do Banco de Dados**

Criar o schema completo no PostgreSQL com as seguintes tabelas:

**Tabelas Principais:**

* **alunos**  
  * id (PK), nome, email (UNIQUE), data\_nascimento, data\_cadastro  
* **instrutores**  
  * id (PK), nome, email (UNIQUE), especialidade, biografia  
* **categorias**  
  * id (PK), nome, descricao  
* **cursos**  
  * id (PK), titulo, descricao, categoria\_id (FK), instrutor\_id (FK), preco, carga\_horaria, nivel (iniciante/intermediario/avancado), data\_criacao  
* **modulos**  
  * id (PK), curso\_id (FK), titulo, ordem, descricao  
* **aulas**  
  * id (PK), modulo\_id (FK), titulo, ordem, duracao\_minutos, tipo (video/texto/quiz)  
* **matriculas**  
  * id (PK), aluno\_id (FK), curso\_id (FK), data\_matricula, data\_conclusao, status (ativa/concluida/cancelada), valor\_pago  
* **progresso\_aulas**  
  * id (PK), matricula\_id (FK), aula\_id (FK), concluida (boolean), data\_conclusao, tempo\_assistido\_minutos  
* **avaliacoes**  
  * id (PK), matricula\_id (FK), curso\_id (FK), nota (1-5), comentario, data\_avaliacao

**Requisitos da Modelagem:**

* ✅ Aplicar normalização (1FN, 2FN, 3FN)  
* ✅ Definir todas as chaves primárias e estrangeiras  
* ✅ Adicionar constraints apropriadas (NOT NULL, UNIQUE, CHECK)  
* ✅ Criar índices em colunas frequentemente consultadas  
* ✅ Documentar o diagrama ER (Entidade-Relacionamento)

**1.2 Inserção de Dados**

Inserir dados de exemplo em todas as tabelas:

* Mínimo de 5 categorias  
* Mínimo de 10 instrutores  
* Mínimo de 20 cursos (variados em preço, nível e categoria)  
* Mínimo de 50 aulas distribuídas entre os cursos  
* Mínimo de 30 alunos  
* Mínimo de 80 matrículas (alguns alunos em vários cursos)  
* Dados de progresso e avaliações variados

💡 **Dica:** Use os scripts Python (Parte 2\) para gerar esses dados\!

**1.3 Consultas SQL Obrigatórias**

**Consultas Básicas (3 consultas):**

1. Listar todos os cursos com nome da categoria e do instrutor  
2. Listar todos os alunos matriculados em um curso específico  
3. Exibir todas as aulas de um curso ordenadas por módulo e ordem

**Consultas com Agregações (4 consultas):** 

	1\. Calcular a média de avaliações de cada curso   
	2\. Contar quantos alunos estão matriculados por curso   
	3\. Calcular o faturamento total por categoria   
	4\. Identificar o curso com maior número de matrículas ativas

**Consultas com JOINs Múltiplos (3 consultas):**   
8\. Listar alunos, cursos matriculados e porcentagem de conclusão   
9\. Relatório completo de um curso: instrutor, número de alunos, média de avaliações, faturamento   
10\. Listar instrutores com quantidade de cursos, total de alunos e média geral de avaliações

Consultas Analíticas Avançadas (2 consultas):   
11\. Top 5 cursos mais rentáveis (considerar valor\_pago das matrículas) 12\. Alunos que não concluíram nenhum curso nos últimos 6 meses

**1.4 Relatórios SQL**

Criar queries para gerar relatórios de negócio:

* Dashboard geral: total de alunos, cursos, matrículas ativas, receita total  
* Cursos com baixa taxa de conclusão (menos de 30% das aulas concluídas)  
* Instrutores mais bem avaliados (média \>= 4.5)  
* Categorias mais populares (por número de matrículas)  
* Análise temporal: matrículas por mês do ano atual

**PARTE 2: Scripts Python Auxiliares (30% do projeto) 🐍**

**2.1 Gerador de Dados Fictícios**

Criar script Python que gera dados realistas para popular o banco:

Arquivo: `gerador_dados.py`

Funções obrigatórias:

* `gerar_alunos(quantidade)` \- Gera dados de alunos com nomes, emails e datas realistas  
* `gerar_instrutores(quantidade)` \- Gera dados de instrutores com especialidades  
* `gerar_cursos(quantidade)` \- Gera cursos com títulos, descrições, preços variados  
* `gerar_aulas(curso_id, quantidade)` \- Gera estrutura de módulos e aulas  
* `gerar_matriculas(quantidade)` \- Gera matrículas distribuídas entre alunos e cursos  
* `exportar_para_csv()` \- Exporta todos os dados gerados para arquivos CSV separados

**Requisitos:**

* Usar biblioteca Faker para gerar nomes, emails, textos  
* Gerar datas realistas (ex: cadastros nos últimos 2 anos)  
* Preços de cursos variados (R$ 49,90 a R$ 499,90)  
* Criar relacionamentos coerentes (matrículas só de cursos/alunos existentes)  
* Exportar em formato CSV pronto para importação no PostgreSQL

**2.2 Validador de Arquivos**

Criar script que valida arquivos CSV antes de importar no banco:

Arquivo: **\``` validador_csv.py` ``**

**Validações obrigatórias:**

* ✅ Verificar se todos os campos obrigatórios estão preenchidos  
* ✅ Validar formato de email  
* ✅ Validar tipos de dados (números, datas)  
* ✅ Verificar valores dentro de ranges válidos (ex: notas entre 1-5)  
* ✅ Detectar duplicatas  
* ✅ Validar integridade referencial (IDs existentes)  
* ✅ Gerar relatório de erros encontrados

**2.3 Processador de Relatórios**

Criar script que processa exports do banco e gera análises:

**Arquivo: `processador_relatorios.py`**

**Funcionalidades:**

* Ler arquivo CSV exportado do banco (resultado de uma query)  
* Calcular estatísticas adicionais (médias, percentuais, rankings)  
* Gerar visualizações simples em texto (ex: gráfico de barras ASCII)  
* Exportar relatório formatado em TXT ou Markdown  
* Identificar insights (ex: "Curso X tem alta taxa de abandono")

**Exemplo de relatórios:**

* Análise de performance de instrutores  
* Comparativo de categorias de cursos  
* Tendências de matrículas ao longo do tempo  
* Perfil de engajamento dos alunos

**2.4 Funções Auxiliares**

**Criar módulo com funções úteis:**

**Arquivo:** `utils.py`

**Funções sugeridas:**

* `formatar_dinheiro(valor)` \- Formata valores monetários  
* `calcular_taxa_conclusao(aulas_concluidas, total_aulas)` \- Calcula percentual  
* `validar_email(email)` \- Valida formato de email  
* `gerar_senha_hash()` \- Simula geração de senha (preparação para API futura)  
* `formatar_data(data)` \- Padroniza formato de datas

### **Requisitos Técnicos:**  **SQL (70% \- FOCO PRINCIPAL):**

* ### ✅ Utilizar PostgreSQL como SGBD

* ### ✅ Aplicar comandos DDL (CREATE TABLE, ALTER TABLE, DROP TABLE)

* ### ✅ Aplicar comandos DML (INSERT, SELECT, UPDATE, DELETE)

* ### ✅ Utilizar JOINs múltiplos (INNER JOIN, LEFT JOIN)

* ### ✅ Usar agregações (COUNT, AVG, SUM, MAX, MIN, GROUP BY, HAVING)

* ### ✅ Aplicar filtros complexos com WHERE (AND, OR, IN, BETWEEN)

* ### ✅ Usar ordenação com ORDER BY

* ### ✅ Implementar subconsultas (subqueries)

* ### ✅ Criar pelo menos 12 consultas SQL distintas

* ### ✅ Script SQL organizado e comentado

* ### ✅ Documentar o schema com comentários ou diagrama ER

#### **Python (30% \- AUXILIAR):**

* ### ✅ Utilizar Python 3.x

* ### ✅ Estruturar código em funções (mínimo 10 funções)

* ### ✅ Usar biblioteca Faker para dados fictícios

* ### ✅ Manipular arquivos CSV para importação/exportação

* ### ✅ Implementar validações com condicionais

* ### ✅ Usar loops para processar múltiplos registros

* ### ✅ Tratamento de erros com try/except

* ### ✅ Código comentado e organizado

* ### ✅ Separar em módulos (.py) diferentes por funcionalidade

#### **Organização Geral:**

* ### 📁 Estrutura de pastas clara

* ### 📄 README.md explicando como executar

* ### 📄 Script SQL separado para criação do schema (`schema.sql`)

* ### 📄 Script SQL com os INSERTs de dados (`dados.sql`)

* ### 📄 Arquivo com todas as consultas (`consultas.sql`)

* ### 📂 Pasta `python/` com todos os scripts .py

* ### 📂 Pasta `data/` com arquivos CSV gerados

* ### 📂 Pasta `docs/` com diagrama ER e documentação

###


## **Apresentação:**

Desenvolvam uma apresentação completa do projeto:

#### **Conteúdo da Apresentação:**

* **Contexto e Problema (2-3 min)**  
  * O que é uma plataforma EduTech?  
  * Que desafios de dados ela enfrenta?  
  * Por que um banco bem modelado é crucial?  
* **Modelagem do Banco de Dados (3-4 min)**  
  * Apresentar diagrama ER  
  * Explicar decisões de modelagem  
  * Mostrar como aplicou normalização  
  * Justificar relacionamentos entre tabelas  
* **Demonstração SQL (4-5 min)**  
  * Executar 3-4 consultas importantes ao vivo  
  * Mostrar resultados de relatórios analíticos  
  * Explicar a lógica das queries complexas  
  * Demonstrar JOINs e agregações  
* **Scripts Python (2-3 min)**  
  * Demonstrar geração de dados fictícios  
  * Mostrar validação de arquivos  
  * Executar processador de relatórios  
  * Explicar como isso prepara para APIs futuras  
* **Aprendizados e Desafios (1-2 min)**  
  * Principais dificuldades encontradas  
  * Soluções criativas implementadas  
  * O que aprenderam no processo

## **Entregáveis da Apresentação:**

**LinkedIn:**

* Post com prints do diagrama ER  
* Exemplo de uma query complexa e resultado  
* Texto explicando o projeto que mencione as tecnologias utilizadas  
* Incluir link do GitHub

**GitHub:**

* Repositório público e organizado  
* README completo com:  
  * Descrição do projeto  
  * Tecnologias utilizadas  
  * Estrutura de pastas  
  * Como executar (passo a passo)  
  * Exemplos de consultas  
  * Capturas de tela  
* Código versionado com commits descritivos  
* Diagrama ER na pasta docs/

# Utilitários {#utilitários}

### **Bancos de Dados Relacionais e PostgreSQL** {#bancos-de-dados-relacionais-e-postgresql}

Bancos de dados relacionais organizam informações em tabelas conectadas por relacionamentos, garantindo integridade e consistência dos dados. PostgreSQL é um dos SGBDs mais utilizados no mercado, oferecendo robustez, recursos avançados de consulta e alta confiabilidade. O modelo relacional permite manter a integridade dos dados através de constraints e relacionamentos bem definidos, essenciais para aplicações back-end e APIs REST.

### **Normalizacao de Dados** {#normalizacao-de-dados}

### A normalização é o processo de organizar dados para reduzir redundância e melhorar a integridade. As três primeiras formas normais são fundamentais:

* ### **1FN:** Elimina grupos repetidos, cada campo contém valor atômico

* ### **2FN:** Remove dependências parciais, cada campo depende da chave completa

* ### **3FN:** Elimina dependências transitivas, campos não-chave depende apenas da chave primária

### Bancos bem normalizados facilitam a manutenção, evitam inconsistências e melhoram a performance.  	**Python e Manipulacao de Dados**

Python é excelente para processar e preparar dados antes de armazená-los em bancos. A biblioteca Faker permite gerar dados realistas para testes. A manipulação de arquivos CSV/JSON em Python é essencial para importar/exportar dados de diversas fontes. Estas habilidades são fundamentais para criar seeds de dados, validar inputs e processar outputs em APIs REST.

### 

**Recursos úteis:**

**SQL e PostgreSQL:**

* [PostgreSQL Documentation](https://www.postgresql.org/docs/)  
* [SQL Tutorial \- W3Schools](https://www.w3schools.com/sql/)  
* [Database Normalization Guide](https://www.guru99.com/database-normalization.html)  
* [PostgreSQL JOIN Types](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-joins/)

**Python:**

* [Faker Documentation](https://faker.readthedocs.io/)  
* [Python CSV Module](https://docs.python.org/3/library/csv.html)  
* [Python JSON Module](https://docs.python.org/3/library/json.html)  
* [Real Python \- Working with Files](https://realpython.com/working-with-files-in-python/)

**Ferramentas:**

* [pgAdmin](https://www.pgadmin.org/) \- Interface gráfica para PostgreSQL  
* [DBeaver](https://dbeaver.io/) \- Cliente SQL universal  
* [draw.io](https://app.diagrams.net/) \- Criar diagramas ER


## Rubrica {#rubrica}

A rubrica é o arquivo utilizado para correção, dentro dela contém todos os critérios de correção.

| Legenda |  |
| :---: | :---: |
| **Vermelho** | Critérios negativos (Os critérios **grifados** são eliminatórios e **podem zerar a nota das demais tecnologias.**) |
| **Amarelo** | Critérios neutros. |
| **Verde** | Critérios positivos. |
| **Azul** | Os critérios **grifados** são extras e opcionais. |

| Tecnologia | Faltou algo | Tudo OK | Majestoso |
| :---: | ----- | ----- | ----- |
| **Modelagem de Banco de Dados (SQL)** | **• O banco não foi criado • Menos de 6 tabelas criadas • Sem chaves primárias/estrangeiras** • Dados não normalizados • Sem relacionamentos entre tabelas • Estrutura confusa ou mal planejada • Tabelas sem dados inseridos  | • Todas as 9 tabelas principais criadas • Chaves primárias e estrangeiras definidas • Relacionamentos básicos  implementados • Normalização aplicada (1FN e 2FN no mínimo) • Dados de exemplo em todas tabelas • Schema funcional e sem erros • Constraints básicas (NOT NULL) | • Modelagem exemplar e bem documentada • Normalização completa (1FN, 2FN, 3FN) • Diagrama ER profissional • Constraints avançadas (UNIQUE, CHECK, DEFAULT) • 🔵 Índices estratégicos para otimização • 🔵 Views para consultas frequentes • 🔵 Comentários nas tabelas (COMMENT ON) • 🔵 Triggers ou Procedures |
| **Consultas SQL** | **• Menos de 8 consultas implementadas • Consultas não funcionam corretamente** • Não usa JOINs • Sem agregações (COUNT, AVG, etc) • Consultas muito simples (apenas SELECT \*) • Queries sem comentários explicativos | • Pelo menos 12 consultas funcionais • Uso correto de JOINs (INNER, LEFT) • Agregações implementadas  (COUNT, AVG, SUM, GROUP BY) • Filtros e ordenação aplicados • HAVING utilizado adequadamente • Consultas respondem aos requisitos • Queries organizadas e comentadas | • Consultas otimizadas e eficientes • Uso avançado de subqueries • Queries complexas com múltiplos JOINs • Análises de negócio profundas • 🔵 CTEs (WITH clause) • 🔵 Window Functions (ROW\_NUMBER, RANK) • 🔵 CASE WHEN para lógicas complexas • 🔵 Queries parametrizáveis • Documentação excelente de cada query |
| **Scripts Python** | **• Não criou scripts Python • Menos de 5 funções implementadas • Scripts não executam** • Não usa Faker ou similar • Não gera arquivos CSV • Código com muitos erros | • Gerador de dados funcional • Usa Faker para dados realistas • Pelo menos 8 funções criadas • Validador de CSV implementado • Exporta dados corretamente • Código organizado em arquivos • Validações básicas funcionam • Comentários explicativos | • Scripts Python muito bem estruturados • Código limpo e profissional • Validações robustas e completas • Tratamento de erros abrangente • Processador de relatórios criativo • 🔵 Type hints em funções • 🔵 Docstrings em todas funções • 🔵 Testes unitários • 🔵 Configurações via arquivo .env • 🔵 Logs de execução • 🔵 Progress bar na geração de dados |
| **Integração SQL \+ Python** | • Arquivos Python e SQL totalmente desconectados • CSVs gerados não importam no banco • Estrutura de dados incompatível • Falta coerência entre as partes | • CSVs gerados são importáveis no PostgreSQL • Estrutura de dados consistente • Validações Python ajudam qualidade SQL • Fluxo de trabalho claro • README explica como usar ambas partes | • Integração fluida e bem pensada • Pipeline de dados completo • CSVs com COPY commands prontos • Scripts automatizam processo • 🔵 Script shell para importação automática • 🔵 Makefile para automação • Documentação do fluxo completo |
| **Relatórios e Análises** | • Não implementa relatórios • Consultas não respondem perguntas de negócio • Sem análises estatísticas | • Relatórios básicos implementados • Dashboard geral funcional • Análises estatísticas corretas • Queries analíticas funcionam • Responde perguntas de negócio | • Relatórios profissionais e detalhados • Análises de negócio profundas • Insights relevantes identificados • 🔵 Visualizações em texto (gráficos ASCII) • 🔵 Export de relatórios formatados • 🔵 Comparativos e tendências • 🔵 Recomendações baseadas em dados |
| **Organização e Boas Práticas** | **• Código totalmente desorganizado**  • Arquivos sem estrutura lógica  • Sem README • Nomes de variáveis ruins • Sem comentários • Código duplicado | • Código organizado em pastas • Estrutura de arquivos clara • README básico presente • Nomes descritivos de variáveis • Comentários explicativos • Scripts SQL organizados • Sem código duplicado significativo | • Estrutura de projeto profissional • Separação clara de responsabilidades • README completo e detalhado • Documentação técnica excelente • Código muito limpo • 🔵 .gitignore apropriado • 🔵 requirements.txt • 🔵 Diagramas na documentação • 🔵 Exemplos de uso no README • 🔵 CHANGELOG ou histórico |
| **Apresentação e Entrega** | **• Sem apresentação • Não publicou no LinkedIn • Não subiu no GitHub** • Sem documentação | • Apresentação realizada • Publicado no LinkedIn • Código no GitHub público • README com instruções básicas • Explica o projeto adequadamente • Demonstra funcionalidades principais | • Apresentação profissional e completa • Post no LinkedIn bem elaborado e engajador • Repositório GitHub muito bem organizado • 🔵 Vídeo demonstrativo (Loom/YouTube) • 🔵 GIFs demonstrativos • 🔵 Badge de tecnologias no README • Documentação digna de portfólio |

**Critérios Eliminatórios (Projeto invalido):**

Atenção\! Os critérios abaixo são **ELIMINATÓRIOS** e resultam projeto invalido:

❌ Não criou o banco de dados no PostgreSQL

❌ Menos de 6 tabelas no banco

❌ Menos de 8 consultas SQL implementadas

❌ Não criou nenhum script Python

❌ Sistema SQL não executa/tem erros graves

❌ Não apresentou o projeto

❌ Não publicou no LinkedIn e GitHub

**Dicas Importantes 💡**

**Para o SQL:**

* Comece pelo diagrama ER antes de criar as tabelas  
* Teste cada query individualmente antes de documentar  
* Use EXPLAIN ANALYZE para otimizar queries lentas  
* Comente suas queries explicando o que fazem

**Para o Python:**

* Use ambientes virtuais (venv) para gerenciar dependências  
* Teste seus scripts com dados pequenos primeiro  
* Valide os CSVs gerados antes de importar no banco  
* Organize funções em módulos lógicos

**Para a Apresentação:**

* Pratique a demonstração antes de apresentar  
* Tenha prints/gravações como backup  
* Explique DECISÕES, não só o que fez  
* Mostre o raciocínio por trás da modelagem

**Boa sorte\! 🚀**

Lembre-se: este projeto simula cenários reais de desenvolvimento back-end. O foco é demonstrar que você domina modelagem de dados e SQL, com Python como ferramenta auxiliar. Estas são as fundações para construir APIs REST robustas no futuro\!

**Foque primeiro em fazer funcionar, depois em refinar e adicionar extras.** O aprendizado está no processo\! 💪