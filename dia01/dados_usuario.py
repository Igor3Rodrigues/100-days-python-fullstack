# Recebe um número inteiro
idade = int(input("Qual a sua idade? "))

# Recebe um número decimal (float)
altura = float(input("Qual a sua altura em metros? "))

# Recebe uma string
nome = input("Qual o seu nome? ")

# Recebe um resposta boolean (sim ou não)
tem_carro = input("Você tem carro? (sim ou não): ").strip().lower()
tem_carro = tem_carro == "sim"

# Recebe os resultados
print("\n===== Resultado =====\n")
print(f"Nome: {nome}\n")
print(f"Idade: {idade} anos\n")
print(f"Altura: {altura:.2f} metros\n")
print(f"Você tem carro? {'Sim' if tem_carro else 'Não'}\n")