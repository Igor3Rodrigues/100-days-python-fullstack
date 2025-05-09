# Funções para as quatro operações básicas
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por zero"
    return a / b

# Interface principal
def calculadora():
    print("\n=== Calculadora Simples ===")
    print("\nOperações disponíveis: +  -  *  /")
    
    try:
        num1 = float(input("\nDigite o primeiro número: "))
        operacao = input("\nDigite o operador (+, -, *, /): ")
        num2 = float(input("\nDigite o segundo número: "))
        
        if operacao == "+":
            resultado = somar(num1, num2)
        elif operacao == "-":
            resultado = subtrair(num1, num2)
        elif operacao == "*":
            resultado = multiplicar(num1, num2)
        elif operacao == "/":
            resultado = dividir(num1, num2)
        else:
            resultado = "Operação inválida"
            
        print(f"\nResultado: {resultado}\n")
    
    except ValueError:
        print("\nErro: insira apenas números válidos.\n")
        
# Executa o programa
calculadora()