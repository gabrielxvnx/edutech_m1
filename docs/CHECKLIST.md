# Checklist do Projeto EduTech

Status de conclusão dos requisitos do projeto, organizado pela legenda de cores da rubrica.

***

### 🔴 Critérios Eliminatórios e Pendências Críticas

* [ ] **Python:** Criar o script `processador_relatorios.py`.
* [ ] **Python:** Criar o script `utils.py`.
* [ ] **Entrega:** Realizar a apresentação do projeto.
* [ ] **Entrega:** Publicar o projeto no LinkedIn e GitHub.
* [ ] **Entrega:** Adicionar o professor como colaborador e abrir o Pull Request.

***

### 🟡 Requisitos Funcionais (Tudo OK)

* [x] **SQL:** Todas as 9 tabelas principais foram criadas.
* [x] **SQL:** Chaves primárias e estrangeiras foram definidas.
* [x] **SQL:** Constraints básicas (`NOT NULL`) foram aplicadas.
* [x] **SQL:** Dados de exemplo existem para todas as tabelas.
* [x] **SQL:** Pelo menos 8 consultas funcionais foram implementadas.
* [x] **SQL:** Uso correto de `JOINs` e agregações.
* [x] **Python:** Script `data_generator.py` é funcional e usa a biblioteca Faker.
* [x] **Python:** Script `csv_validator.py` está implementado com validações básicas.
* [x] **Python:** Os dados gerados são exportados para arquivos CSV.
* [x] **Organização:** A estrutura de pastas do projeto está clara.
* [x] **Organização:** Os scripts SQL estão separados e organizados.
* [ ] **SQL:** Criar as queries específicas para os relatórios de negócio.
* [ ] **Python:** Implementar a detecção de duplicatas no `csv_validator.py`.
* [ ] **Python:** Fazer o `csv_validator.py` gerar um arquivo de relatório de erros.
* [ ] **Documentação:** Completar o `README.md` com todas as seções obrigatórias.
* [ ] **Documentação:** Documentar textualmente o Diagrama ER.

***

### 🟢 Critérios Positivos (Majestoso)

* [x] **SQL:** Uso de constraints avançadas (`UNIQUE`, `CHECK`).
* [x] **SQL:** Criação de índices para otimização.
* [x] **SQL:** Criação de `VIEWs` para abstrair a complexidade.
* [x] **Organização:** Uso de `.gitignore` e `requirements.txt`.
* [ ] **SQL:** Uso de `CTEs` (cláusula `WITH`) ou `Window Functions` nas consultas.
* [ ] **Python:** Adicionar `Type Hints` e `Docstrings` nas funções.
* [ ] **Python:** Implementar tratamento de erros mais abrangente com `try/except`.
* [ ] **Python:** Gerar visualizações em modo texto (gráficos ASCII) no `processador_relatorios.py`.
* [ ] **Documentação:** Criar uma documentação técnica de alta qualidade.

***

### 🔵 Critérios Extras (Opcionais)

* [ ] **SQL:** Implementar `Triggers` ou `Procedures`.
* [ ] **Python:** Criar testes unitários para os scripts.
* [ ] **Python:** Adicionar logs de execução.
* [ ] **Automação:** Criar um `Makefile` ou script `shell` para automatizar o fluxo de execução.
* [ ] **Apresentação:** Criar um vídeo ou GIFs demonstrativos do projeto.

