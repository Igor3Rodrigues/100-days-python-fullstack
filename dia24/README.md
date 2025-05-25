# 📘 Dia 24/100 — Desafio 100 Dias de Código

Hoje implementei rotas dinâmicas no projeto Blog com Flask. Agora cada post pode ser acessado por uma URL única baseada no seu ID, como `/posts/1`. Isso foi possível usando parâmetros dinâmicos com `<int:id>` nas rotas e realizando a busca pelo post correspondente no backend.

## 🛠️ O que foi praticado

- Criação de rotas dinâmicas com Flask (`/posts/<int:id>`)
- Filtragem de dados com base em parâmetros da URL
- Renderização condicional de templates
- Exibição da página com conteúdo completo do post

## 💡 O que aprendi

- Como capturar parâmetros da URL com Flask
- Como buscar dados específicos em uma lista/dicionário
- Tratamento de erros simples quando o post não é encontrado

## 📘 Recursos utilizados

- [Documentação oficial do Flask](https://flask.palletsprojects.com/)
- Exemplos da comunidade no GitHub

## 📈 Dificuldade

**6/10** — A estrutura da rota foi simples, mas a busca correta do post e o retorno da página exigiram atenção à lógica.

---
