# Criando e manipulando uma lista de tarefas
tarefas = ["Estudar Python", "Fazer exercícios", "Ler documentação"]

# Adicionando uma nova tarefa à lista
tarefas.append("Revisar conceitos")

# Removendo uma tarefa específica
tarefas.remove("Fazer exercícios")

# Exibindo todas as tarefas
print("📋 Lista de Tarefas:")
for tarefa in tarefas:
    print(f"- {tarefa}")

print("\n")

# Criando um dicionário com informações de um usuário
usuario = {
    "nome": "Igor",
    "idade": 25,
    "linguagem": "Python"
}

# Acessando dados do dicionário
print("👤 Informações do usuário:")
print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")
print(f"Linguagem favorita: {usuario['linguagem']}")

# Atualizando valor de uma chave
usuario["idade"] = 27

# Adicionando nova chave ao dicionário
usuario["experiência"] = "Intermediário"

print("\n👤 Dados atualizados:")
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}")
