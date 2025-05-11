# Funções de operações matemáticas
def somar(a, b):
    """Função que soma dois números"""
    return a + b

def subtrair(a, b):
    """Função que subtrai dois números"""
    return a - b

def multiplicar(a, b):
    """Função que multiplica dois números"""
    return a * b

def dividir(a, b):
    """Função que divide dois números com verificação de divisão por zero"""
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

# Dicionário para associar operações às funções
operacoes = {
    "+": somar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir
}

# Lista para armazenar o histórico de operações
historico = []

# Função principal da calculadora
def calculadora():
    print("=== Calculadora Interativa ===")
    
    while True:
        # Menu de operações
        print("\nEscolha uma operação:\n")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Histórico")
        print("6. Sair")
        
        opcao = input("\nDigite o número da opção desejada: ")

        # Opção para sair do programa
        if opcao == "6":
            print("\nSaindo do programa. Até logo!\n")
            break
        
        # Opção para ver o histórico
        elif opcao == "5":
            print("\nHistórico de operações:\n")
            if not historico:
                print("Nenhuma operação realizada ainda.\n")
            else:
                for item in historico:
                    print(f"{item['entrada']} = {item['resultado']}")
                print()  # quebra de linha ao final

        # Verificação se a opção é válida
        elif opcao in ["1", "2", "3", "4"]:
            try:
                # Solicitar valores ao usuário
                num1 = float(input("\nDigite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                # Realizar a operação com base na opção escolhida
                if opcao == "1":
                    resultado = somar(num1, num2)
                elif opcao == "2":
                    resultado = subtrair(num1, num2)
                elif opcao == "3":
                    resultado = multiplicar(num1, num2)
                elif opcao == "4":
                    resultado = dividir(num1, num2)

                # Armazenar a operação e o resultado no histórico
                operacao = "+" if opcao == "1" else "-" if opcao == "2" else "*" if opcao == "3" else "/"
                entrada = f"{num1} {operacao} {num2}"
                historico.append({"entrada": entrada, "resultado": resultado})
                
                # Exibir o resultado com quebras de linha
                print(f"\nResultado: {resultado}\n")

            except ValueError:
                print("\nErro: Por favor, insira números válidos.\n")

        else:
            print("\nOpção inválida. Tente novamente.\n")

# Chamada da função principal
calculadora()
