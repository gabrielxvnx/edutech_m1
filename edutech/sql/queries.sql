-- Consultas Básicas

-- 1. Listar todos os cursos com nome da categoria e do instrutor
SELECT curso_id, curso_titulo, categoria_nome, instrutor_nome, instrutor_especialidade
FROM vw_cursos_detalhes
ORDER BY categoria_nome, curso_titulo;

-- 2. Listar todos os alunos matriculados em um curso específico
SELECT aluno_id, aluno_nome, aluno_email, data_matricula, status_matricula
FROM vw_alunos_por_curso
WHERE curso_id = 1  -- Substitua pelo ID do curso desejado
ORDER BY aluno_nome;

-- 3. Exibir todas as aulas de um curso ordenadas por módulo e ordem
SELECT modulo_ordem, modulo_titulo, aula_titulo, duracao_minutos
FROM vw_aulas_por_curso
WHERE curso_id = 1  -- Substitua pelo ID do curso desejado
ORDER BY modulo_ordem, aula_id;

-- Consultas com Agregações

-- 4. Calcular a média de avaliações de cada curso
SELECT curso_id, titulo, media_avaliacoes, total_avaliacoes
FROM vw_media_avaliacoes_curso
ORDER BY media_avaliacoes DESC;

-- 5. Contar quantos alunos estão matriculados por curso
SELECT curso_id, titulo, total_alunos, alunos_ativos
FROM vw_alunos_matriculados_curso
ORDER BY total_alunos DESC;

-- 6. Calcular o faturamento total por categoria
SELECT categoria_nome, total_cursos, faturamento_total
FROM vw_faturamento_categoria
ORDER BY faturamento_total DESC;

-- 7. Identificar o curso com maior número de matrículas ativas
SELECT curso_id, titulo, alunos_ativos
FROM vw_alunos_matriculados_curso
WHERE alunos_ativos > 0
ORDER BY alunos_ativos DESC
LIMIT 1;

-- Consultas com JOINs Múltiplos

-- 8. Listar alunos, cursos matriculados e porcentagem de conclusão
SELECT 
    a.nome as aluno_nome,
    c.titulo as curso_titulo,
    p.porcentagem_conclusao
FROM alunos a
JOIN vw_progresso_alunos p ON a.id = p.aluno_id
JOIN cursos c ON p.curso_id = c.id
ORDER BY a.nome, c.titulo;

-- 9. Relatório completo de um curso
SELECT *
FROM vw_relatorio_curso
WHERE curso_id = 1;  -- Substitua pelo ID do curso desejado

-- 10. Listar instrutores com quantidade de cursos, total de alunos e média geral de avaliações
SELECT *
FROM vw_desempenho_instrutores
ORDER BY total_alunos DESC;

-- Consultas Analíticas Avançadas

-- 11. Top 5 cursos mais rentáveis
SELECT 
    curso_id,
    titulo,
    categoria,
    instrutor,
    total_alunos,
    faturamento_total,
    media_avaliacoes
FROM vw_cursos_mais_rentaveis
ORDER BY faturamento_total DESC
LIMIT 5;
