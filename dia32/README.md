# Dia 32/100 - Relacionamentos e consultas mais complexas

Hoje pratiquei a criação de relacionamentos entre tabelas no SQLite com chaves estrangeiras e JOINs para unir dados entre usuários e tarefas.

## 📚 Conteúdo Estudado

- `INNER JOIN` entre usuários e tarefas
- Filtros com `WHERE`, `LIKE`, `LIMIT`, `ORDER BY`
- Modelagem de dados relacional simples

## 💻 Exemplo de Consulta

```sql
SELECT tarefas.titulo, usuarios.nome
FROM tarefas
INNER JOIN usuarios ON tarefas.usuario_id = usuarios.id;
```
