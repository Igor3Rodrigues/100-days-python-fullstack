# 📅 Dia 19 — Herança de Templates com Jinja2

Hoje aprendi a utilizar **herança de templates** para evitar duplicação de HTML entre as páginas do meu projeto Flask.

## 🧠 Aprendizado
- Criar um `base.html` com estrutura base do site
- Usar `{% block content %}` para definir áreas variáveis
- Usar `{% extends "base.html" %}` nas páginas filhas

## 💻 O que fiz
- Estruturei um layout principal (base.html)
- Criei `index.html` e `sobre.html` herdando o layout
- Adicionei navegação básica entre páginas

## 🚀 Dificuldade
Nível 4/10 — Ótimo para treinar organização de código e evitar repetições.

## 📚 Recursos
- [Documentação Flask - Templates](https://flask.palletsprojects.com/)
- [Jinja2 Blocks - W3Schools](https://www.w3schools.com/python/gloss_python_jinja2_template_blocks.asp)
