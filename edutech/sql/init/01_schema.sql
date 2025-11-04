-- 01_schema.sql

-- CATEGORIAS
CREATE TABLE IF NOT EXISTS categorias (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE,
    descricao VARCHAR(300) NOT NULL
);

-- INSTRUTORES
CREATE TABLE IF NOT EXISTS instrutores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    especialidade VARCHAR(50) NOT NULL,
    biografia VARCHAR(300) NOT NULL,
    email VARCHAR(100) UNIQUE,
    CONSTRAINT chk_email_instrutores CHECK (email LIKE '%_@__%.__%')
);

-- CURSOS
CREATE TABLE IF NOT EXISTS cursos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    descricao VARCHAR(300) NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    categoria_id INT NOT NULL REFERENCES categorias(id) ON DELETE RESTRICT,
    instrutor_id INT REFERENCES instrutores(id) ON DELETE SET NULL, -- permite NULL para ON DELETE SET NULL
    carga_horaria INT NOT NULL,
    nivel VARCHAR(20) NOT NULL CHECK (nivel IN ('iniciante', 'intermediario', 'avancado')),
    preco NUMERIC(10,2),     -- coluna adicionada para index
    data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_data_fim CHECK (data_fim > data_inicio),
    CONSTRAINT chk_carga_horaria CHECK (carga_horaria > 0)
);

-- MODULOS (depende de cursos)
CREATE TABLE IF NOT EXISTS modulos (
    id SERIAL PRIMARY KEY,
    curso_id INT NOT NULL REFERENCES cursos(id) ON DELETE CASCADE,
    titulo VARCHAR(100) NOT NULL,
    descricao VARCHAR(300) NOT NULL,
    ordem INT NOT NULL,
    CONSTRAINT chk_ordem_modulo CHECK (ordem > 0),
    CONSTRAINT uk_curso_ordem_modulo UNIQUE (curso_id, ordem)
);

-- AULAS (depende de modulos)
CREATE TABLE IF NOT EXISTS aulas (
    id SERIAL PRIMARY KEY,
    modulo_id INT NOT NULL REFERENCES modulos(id) ON DELETE CASCADE,
    titulo VARCHAR(200) NOT NULL,
    duracao_minutos INT DEFAULT 0,
    conteudo TEXT
);

-- ALUNOS
CREATE TABLE IF NOT EXISTS alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    data_cadastro DATE NOT NULL DEFAULT CURRENT_DATE,
    email VARCHAR(100) UNIQUE NOT NULL,
    CONSTRAINT chk_email_aluno CHECK (email LIKE '%_@__%.__%'),
    CONSTRAINT chk_data_nascimento CHECK (data_nascimento < data_cadastro)
);

-- MATRICULAS (depende de alunos e cursos)
CREATE TABLE IF NOT EXISTS matriculas (
    id SERIAL PRIMARY KEY,
    aluno_id INT NOT NULL REFERENCES alunos(id) ON DELETE CASCADE,
    curso_id INT NOT NULL REFERENCES cursos(id) ON DELETE CASCADE,
    data_matricula TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_conclusao DATE,
    status VARCHAR(20) NOT NULL DEFAULT 'ativa',
    valor_pago NUMERIC(10,2),
    CONSTRAINT chk_status CHECK (status IN ('ativa', 'concluida', 'cancelada')),
    CONSTRAINT chk_data_conclusao CHECK (data_conclusao IS NULL OR data_conclusao > data_matricula),
    CONSTRAINT uk_aluno_curso UNIQUE (aluno_id, curso_id),
    CONSTRAINT chk_valor_pago CHECK (valor_pago >= 0)
);

-- PROGRESSO AULAS (depende de matriculas e aulas)
CREATE TABLE IF NOT EXISTS progresso_aulas (
    id SERIAL PRIMARY KEY,
    matricula_id INTEGER NOT NULL REFERENCES matriculas(id) ON DELETE CASCADE,
    aula_id INTEGER NOT NULL REFERENCES aulas(id) ON DELETE CASCADE,
    concluida BOOLEAN DEFAULT FALSE,
    data_conclusao TIMESTAMP,
    tempo_assistido_minutos INTEGER DEFAULT 0,
    CONSTRAINT chk_tempo_assistido CHECK (tempo_assistido_minutos >= 0),
    CONSTRAINT uk_matricula_aula UNIQUE (matricula_id, aula_id)
);

-- AVALIACOES (depende de matriculas e cursos)
CREATE TABLE IF NOT EXISTS avaliacoes (
    id SERIAL PRIMARY KEY,
    matricula_id INT NOT NULL REFERENCES matriculas(id) ON DELETE CASCADE,
    curso_id INT NOT NULL REFERENCES cursos(id) ON DELETE CASCADE,
    nota INT NOT NULL,
    comentario VARCHAR(300),
    data_avaliacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_nota CHECK (nota >= 1 AND nota <= 10),
    CONSTRAINT uk_matricula_avaliacao UNIQUE (matricula_id, curso_id)
);

-- INDEXES
CREATE INDEX IF NOT EXISTS idx_alunos_email ON alunos(email);
CREATE INDEX IF NOT EXISTS idx_alunos_data_cadastro ON alunos(data_cadastro);
CREATE INDEX IF NOT EXISTS idx_instrutores_especialidade ON instrutores(especialidade);
CREATE INDEX IF NOT EXISTS idx_cursos_categoria ON cursos(categoria_id);
CREATE INDEX IF NOT EXISTS idx_cursos_instrutor ON cursos(instrutor_id);
CREATE INDEX IF NOT EXISTS idx_cursos_nivel ON cursos(nivel);
CREATE INDEX IF NOT EXISTS idx_cursos_preco ON cursos(preco);
CREATE INDEX IF NOT EXISTS idx_modulos_curso ON modulos(curso_id);
CREATE INDEX IF NOT EXISTS idx_aulas_modulo ON aulas(modulo_id);
CREATE INDEX IF NOT EXISTS idx_matriculas_aluno ON matriculas(aluno_id);
CREATE INDEX IF NOT EXISTS idx_matriculas_curso ON matriculas(curso_id);
CREATE INDEX IF NOT EXISTS idx_matriculas_status ON matriculas(status);
CREATE INDEX IF NOT EXISTS idx_matriculas_data ON matriculas(data_matricula);
CREATE INDEX IF NOT EXISTS idx_progresso_matricula ON progresso_aulas(matricula_id);
CREATE INDEX IF NOT EXISTS idx_progresso_aula ON progresso_aulas(aula_id);
CREATE INDEX IF NOT EXISTS idx_progresso_concluida ON progresso_aulas(concluida);
CREATE INDEX IF NOT EXISTS idx_avaliacoes_curso ON avaliacoes(curso_id);
CREATE INDEX IF NOT EXISTS idx_avaliacoes_nota ON avaliacoes(nota);
