SELECT c.cliente_id, c.nome, t.numero
FROM Clientes c
JOIN Telefones t ON c.cliente_id = t.cliente_id
JOIN Estados e ON c.estado_id = e.estado_id
WHERE e.sigla = 'SP';
