# Documentação do Modelo de Dados - EduTech

Neste documento, eu detalho as decisões de modelagem que tomei para a estrutura do banco de dados da plataforma EduTech. O objetivo foi criar um schema normalizado, coeso e performático para suportar as funcionalidades de um sistema de gerenciamento de cursos online.

---

## Diagrama Entidade-Relacionamento (ER)

A imagem abaixo representa a estrutura visual do banco de dados, incluindo todas as tabelas e seus relacionamentos.

![Diagrama ER do Banco de Dados](drawSQL-image-export-2025-10-26%20(1).png)

---

## Detalhamento das Tabelas e Decisões de Modelagem

### Tabelas Principais

#### 1. `categorias`, `instrutores` e `alunos`
- **Propósito:** Estas são as tabelas de base do sistema. `categorias` armazena os tipos de cursos, `instrutores` guarda as informações dos professores e `alunos` contém os dados dos usuários que consomem os cursos.
- **Decisões:**
    - Eu defini a coluna `email` como `UNIQUE` nas tabelas `instrutores` e `alunos` para garantir que não haja duplicidade de usuários.
    - Adicionei uma constraint `CHECK` para validar o formato básico do email, garantindo uma camada inicial de consistência dos dados.

#### 2. `cursos`
- **Propósito:** É a tabela central do sistema, que conecta um curso a uma categoria e a um instrutor.
- **Decisões de Relacionamento:**
    - **`categoria_id`:** A relação com `categorias` usa `ON DELETE RESTRICT`. Tomei essa decisão para impedir a exclusão de uma categoria que ainda tenha cursos associados, evitando inconsistências.
    - **`instrutor_id`:** A relação com `instrutores` usa `ON DELETE SET NULL`. Essa abordagem permite que um instrutor seja removido do sistema sem apagar os cursos que ele criou. Os cursos permanecerão na plataforma, podendo ter um novo instrutor associado posteriormente.
    - **Constraints:** Utilizei `CHECK` para garantir que o `nivel` do curso seja um dos valores permitidos (`iniciante`, `intermediario`, `avancado`) e que a data de fim seja sempre posterior à data de início.

### Tabelas de Estrutura do Curso

#### 3. `modulos` e `aulas`
- **Propósito:** Elas estruturam o conteúdo de um curso. Um curso é dividido em `modulos`, e cada módulo é composto por `aulas`.
- **Decisões de Relacionamento:**
    - Eu optei por usar `ON DELETE CASCADE` nos relacionamentos `cursos -> modulos` e `modulos -> aulas`. Isso significa que, ao deletar um curso, todos os seus módulos e aulas são automaticamente removidos. Essa decisão simplifica a gestão do ciclo de vida de um curso e mantém a base de dados limpa.
    - Na tabela `modulos`, adicionei uma constraint `UNIQUE` na combinação `(curso_id, ordem)` para garantir que não existam dois módulos com a mesma ordem dentro de um mesmo curso.

### Tabelas de Atividade do Aluno

#### 4. `matriculas`
- **Propósito:** É uma tabela de junção que representa o relacionamento `N:M` (muitos-para-muitos) entre `alunos` e `cursos`.
- **Decisões:**
    - A constraint `UNIQUE` em `(aluno_id, curso_id)` foi crucial para impedir que um mesmo aluno se matricule mais de uma vez no mesmo curso.
    - O uso de `ON DELETE CASCADE` para `aluno_id` e `curso_id` garante que, se um aluno ou um curso for removido do sistema, todas as matrículas associadas a ele também sejam removidas, evitando registros órfãos.

#### 5. `progresso_aulas`
- **Propósito:** Rastreia o avanço de um aluno em cada aula de um curso no qual ele está matriculado.
- **Decisões:**
    - A tabela se conecta diretamente a `matriculas` e `aulas`. A chave primária da matrícula (`matricula_id`) é usada para identificar unicamente a jornada de um aluno em um curso.
    - Assim como em `matriculas`, a constraint `UNIQUE(matricula_id, aula_id)` impede registros duplicados de progresso.

#### 6. `avaliacoes`
- **Propósito:** Armazena as notas e comentários que um aluno (identificado por sua matrícula) atribui a um curso.
- **Decisões:**
    - A constraint `CHECK` na coluna `nota` (entre 1 e 10) garante que as avaliações estejam sempre dentro de um intervalo válido.
    - A chave única em `(matricula_id, curso_id)` garante que um aluno possa avaliar um curso apenas uma vez por matrícula, o que é a regra de negócio padrão para sistemas de avaliação.