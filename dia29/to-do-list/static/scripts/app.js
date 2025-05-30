document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("#task-form");
  const input = document.querySelector("#task-input");
  const taskList = document.querySelector("#task-list");

  let tasks = JSON.parse(localStorage.getItem("tasks")) || [];

  function saveTasks() {
    localStorage.setItem("tasks", JSON.stringify(tasks));
  }

  function createTaskElement(task, index) {
    const li = document.createElement("li");
    const span = document.createElement("span");
    const removeBtn = document.createElement("button");

    span.textContent = task.text;
    removeBtn.textContent = "🗑️";
    removeBtn.classList.add("remove-btn");

    if (task.completed) {
      span.classList.add("task-completed");
    }

    // Toggle tarefa concluída
    span.addEventListener("click", () => {
      task.completed = !task.completed;
      span.classList.toggle("task-completed");
      saveTasks();
    });

    // Remover tarefa
    removeBtn.addEventListener("click", () => {
      tasks.splice(index, 1);
      saveTasks();
      li.remove();
    });

    li.appendChild(span);
    li.appendChild(removeBtn);
    return li;
  }

  function renderTasks() {
    taskList.innerHTML = "";
    tasks.forEach((task, index) => {
      const taskElement = createTaskElement(task, index);
      taskList.appendChild(taskElement);
    });
  }

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const taskText = input.value.trim();
    if (taskText === "") return;

    const newTask = { text: taskText, completed: false };
    tasks.push(newTask);
    saveTasks();

    const taskElement = createTaskElement(newTask, tasks.length - 1);
    taskList.appendChild(taskElement);
    input.value = "";
  });

  renderTasks();
});
