# Exemplo 1: Tratando divisão por zero
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Você deve digitar um número inteiro.")

# Exemplo 2: Tratando erro de índice em listas
lista = [1, 2, 3]

try:
    indice = int(input("\nDigite o índice que deseja acessar na lista [0, 1, 2]: "))
    print(f"Valor no índice {indice}: {lista[indice]}")
except IndexError:
    print("Erro: Índice fora do intervalo da lista.")
except ValueError:
    print("Erro: Índice deve ser um número inteiro.")