<script>
  // Seleciona os elementos do DOM
  const form = document.querySelector("form");
  const input = document.querySelector("#task-input");
  const taskList = document.querySelector("#task-list");

  // Função para adicionar uma nova tarefa
  form.addEventListener("submit", function (e) {
    e.preventDefault(); // Evita recarregar a página

    const taskText = input.value.trim();
    if (taskText === "") return; // Valida entrada vazia

    // Cria o elemento da tarefa
    const li = document.createElement("li");
    li.textContent = taskText;

    // Adiciona à lista
    taskList.appendChild(li);

    // Limpa o campo
    input.value = "";
  });
</script>
