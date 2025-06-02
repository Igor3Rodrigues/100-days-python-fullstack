document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("#task-form");
  const input = document.querySelector("#task-input");
  const taskList = document.querySelector("#task-list");

  // Recupera tarefas do DOM
  function getTasksFromDOM() {
    const tasks = [];
    taskList.querySelectorAll("li").forEach((li) => {
      const span = li.querySelector("span");
      tasks.push({
        text: span.textContent,
        completed: span.classList.contains("task-completed"),
      });
    });
    return tasks;
  }

  // Salva tarefas no localStorage
  function saveTasks() {
    const tasks = getTasksFromDOM();
    localStorage.setItem("tasks", JSON.stringify(tasks));
  }

  // Adiciona tarefa ao DOM
  function addTask(text, completed = false) {
    const li = document.createElement("li");
    const span = document.createElement("span");
    const removeBtn = document.createElement("button");

    span.textContent = text;
    if (completed) span.classList.add("task-completed");

    removeBtn.textContent = "🗑️";
    removeBtn.classList.add("remove-btn");

    // Marcar como concluída
    span.addEventListener("click", () => {
      span.classList.toggle("task-completed");
      saveTasks();
    });

    // Remover tarefa
    removeBtn.addEventListener("click", () => {
      li.remove();
      saveTasks();
    });

    li.appendChild(span);
    li.appendChild(removeBtn);
    taskList.appendChild(li);
  }

  // Carrega tarefas salvas
  const savedTasks = JSON.parse(localStorage.getItem("tasks")) || [];
  savedTasks.forEach((task) => addTask(task.text, task.completed));

  // Evento de adicionar nova tarefa
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if (text === "") return;
    addTask(text);
    input.value = "";
    saveTasks();
  });
});
