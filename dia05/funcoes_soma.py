# Definindo uma função que recebe dois parâmetros e retorna a soma
def soma(a, b):
    """
    Esta função recebe dois números (a e b)
    e retorna a soma entre eles.
    """
    return a + b

# Função que exibe o resultado da soma
def mostrar_resultado():
    # Solicitando entrada do usuário
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Chamando a função soma e armazenando o resultado
    resultado = soma(num1, num2)
    
    # Exibindo o resultado
    print(f"\nA soma entre o {num1} e {num2} é {resultado}\n")
    
# Chamando a função principal
mostrar_resultado()  