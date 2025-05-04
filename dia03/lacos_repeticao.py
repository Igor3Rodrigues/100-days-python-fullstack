# Exemplo 1: Usando o laço for para iterar sobre uma lista de frutas
frutas = ["maçã", "banana", "laranja", "uva"]

print("Frutas disponíveis:")
for fruta in frutas:
    # Para cada item na lista, imprimimos a fruta
    print(f"- {fruta}")

print("\n")  # Linha em branco

# Exemplo 2: Usando o laço while para repetir até o usuário digitar 'sair'
entrada = ""

print("Digite algo (ou 'sair' para encerrar):")
while entrada.lower() != "sair":
    entrada = input(">>> ")
    if entrada.lower() != "sair":
        print(f"Você digitou: {entrada}")

print("Programa encerrado.")
