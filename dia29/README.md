# 🧩 Dia 29/100 — Eventos e interações na To-do List

Neste dia, adicionei mais interatividade ao projeto, permitindo **marcar tarefas como concluídas** e **remover** itens da lista.

## ✅ Funcionalidades adicionadas:

- Clicar no nome da tarefa risca o texto (toggle de classe `.completed`)
- Botão de lixeira para remover tarefa da lista
- Estilo visual diferenciado para tarefas finalizadas

## 🧠 Conceitos aplicados:

- `addEventListener("click", ...)`
- `classList.toggle()` para mudar o estilo
- `remove()` para excluir elementos do DOM
- Criação de botões dinâmicos com eventos

## 🎨 CSS adicional:

```css
.completed {
  text-decoration: line-through;
  color: #888;
}
```
