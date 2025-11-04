-- Views para consultas básicas
CREATE OR REPLACE VIEW vw_cursos_detalhes AS
SELECT 
    c.id as curso_id,
    c.titulo as curso_titulo,
    c.descricao as curso_descricao,
    c.nivel,
    c.preco,
    cat.id as categoria_id,
    cat.nome as categoria_nome,
    i.id as instrutor_id,
    i.nome as instrutor_nome,
    i.especialidade as instrutor_especialidade
FROM cursos c
JOIN categorias cat ON c.categoria_id = cat.id
JOIN instrutores i ON c.instrutor_id = i.id;

CREATE OR REPLACE VIEW vw_alunos_por_curso AS
SELECT 
    c.id as curso_id,
    c.titulo as curso_titulo,
    a.id as aluno_id,
    a.nome as aluno_nome,
    a.email as aluno_email,
    m.data_matricula,
    m.status as status_matricula
FROM cursos c
JOIN matriculas m ON c.id = m.curso_id
JOIN alunos a ON m.aluno_id = a.id;

CREATE OR REPLACE VIEW vw_aulas_por_curso AS
SELECT 
    c.id as curso_id,
    c.titulo as curso_titulo,
    m.id as modulo_id,
    m.titulo as modulo_titulo,
    m.ordem as modulo_ordem,
    a.id as aula_id,
    a.titulo as aula_titulo,
    a.duracao_minutos,
    a.conteudo
FROM cursos c
JOIN modulos m ON c.id = m.curso_id
JOIN aulas a ON m.id = a.modulo_id
ORDER BY c.id, m.ordem, a.id;

-- Views para consultas com agregações
CREATE OR REPLACE VIEW vw_media_avaliacoes_curso AS
SELECT 
    c.id as curso_id,
    c.titulo,
    COALESCE(AVG(av.nota), 0) as media_avaliacoes,
    COUNT(av.id) as total_avaliacoes
FROM cursos c
LEFT JOIN avaliacoes av ON c.id = av.curso_id
GROUP BY c.id, c.titulo;

CREATE OR REPLACE VIEW vw_alunos_matriculados_curso AS
SELECT 
    c.id as curso_id,
    c.titulo,
    COUNT(DISTINCT m.aluno_id) as total_alunos,
    COUNT(DISTINCT CASE WHEN m.status = 'ativa' THEN m.aluno_id END) as alunos_ativos
FROM cursos c
LEFT JOIN matriculas m ON c.id = m.curso_id
GROUP BY c.id, c.titulo;

CREATE OR REPLACE VIEW vw_faturamento_categoria AS
SELECT 
    cat.id as categoria_id,
    cat.nome as categoria_nome,
    COUNT(DISTINCT c.id) as total_cursos,
    COALESCE(SUM(m.valor_pago), 0) as faturamento_total
FROM categorias cat
LEFT JOIN cursos c ON cat.id = c.categoria_id
LEFT JOIN matriculas m ON c.id = m.curso_id
GROUP BY cat.id, cat.nome;

-- Views para consultas com JOINs múltiplos
CREATE OR REPLACE VIEW vw_progresso_alunos AS
SELECT 
    m.aluno_id,
    m.curso_id,
    COUNT(DISTINCT a.id) as total_aulas,
    COUNT(DISTINCT CASE WHEN pa.concluida THEN pa.aula_id END) as aulas_concluidas,
    ROUND(COUNT(DISTINCT CASE WHEN pa.concluida THEN pa.aula_id END)::numeric / 
          NULLIF(COUNT(DISTINCT a.id), 0) * 100, 2) as porcentagem_conclusao
FROM matriculas m
JOIN modulos mod ON m.curso_id = mod.curso_id
JOIN aulas a ON mod.id = a.modulo_id
LEFT JOIN progresso_aulas pa ON m.id = pa.matricula_id AND a.id = pa.aula_id
GROUP BY m.aluno_id, m.curso_id;

CREATE OR REPLACE VIEW vw_relatorio_curso AS
SELECT 
    c.id as curso_id,
    c.titulo,
    i.nome as instrutor,
    i.especialidade,
    COUNT(DISTINCT m.aluno_id) as total_alunos,
    COUNT(DISTINCT CASE WHEN m.status = 'ativa' THEN m.aluno_id END) as alunos_ativos,
    COALESCE(AVG(av.nota), 0) as media_avaliacoes,
    COUNT(av.id) as total_avaliacoes,
    COALESCE(SUM(m.valor_pago), 0) as faturamento_total
FROM cursos c
JOIN instrutores i ON c.instrutor_id = i.id
LEFT JOIN matriculas m ON c.id = m.curso_id
LEFT JOIN avaliacoes av ON c.id = av.curso_id
GROUP BY c.id, c.titulo, i.nome, i.especialidade;

CREATE OR REPLACE VIEW vw_desempenho_instrutores AS
SELECT 
    i.id as instrutor_id,
    i.nome,
    i.especialidade,
    COUNT(DISTINCT c.id) as total_cursos,
    COUNT(DISTINCT m.aluno_id) as total_alunos,
    COALESCE(AVG(av.nota), 0) as media_avaliacoes_geral
FROM instrutores i
LEFT JOIN cursos c ON i.id = c.instrutor_id
LEFT JOIN matriculas m ON c.id = m.curso_id
LEFT JOIN avaliacoes av ON c.id = av.curso_id
GROUP BY i.id, i.nome, i.especialidade;

-- Views para consultas analíticas avançadas
CREATE OR REPLACE VIEW vw_cursos_mais_rentaveis AS
SELECT 
    c.id as curso_id,
    c.titulo,
    cat.nome as categoria,
    i.nome as instrutor,
    COUNT(DISTINCT m.aluno_id) as total_alunos,
    COALESCE(SUM(m.valor_pago), 0) as faturamento_total,
    COALESCE(AVG(av.nota), 0) as media_avaliacoes
FROM cursos c
JOIN categorias cat ON c.categoria_id = cat.id
JOIN instrutores i ON c.instrutor_id = i.id
LEFT JOIN matriculas m ON c.id = m.curso_id
LEFT JOIN avaliacoes av ON c.id = av.curso_id
GROUP BY c.id, c.titulo, cat.nome, i.nome;

CREATE OR REPLACE VIEW vw_alunos_sem_conclusao AS
SELECT 
    a.id as aluno_id,
    a.nome,
    a.email,
    COUNT(DISTINCT m.curso_id) as total_cursos_matriculados,
    COUNT(DISTINCT CASE WHEN m.status = 'ativa' THEN m.curso_id END) as cursos_ativos,
    MAX(m.data_matricula) as ultima_matricula
FROM alunos a
JOIN matriculas m ON a.id = m.aluno_id
WHERE m.status != 'concluida' 
    AND m.data_matricula < CURRENT_DATE - INTERVAL '6 months'
GROUP BY a.id, a.nome, a.email;
