# Funções de operações matemáticas
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

# Dicionário para associar a operação à função
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
    print("=== Calculadora com histórico ===")
    while True:
        print(f"\nDigite 'sair' para encerrar.")
        entrada = input("\nDigite a operação (ex: 5 + 3): ")
        
        if entrada.lower() == "sair":
            break
        
        try:
            partes = entrada.split()
            num1 = float(partes[0])
            op = partes[1]
            num2 = float(partes[2])

            if op in operacoes:
                resultado = operacoes[op](num1, num2)
                historico.append({"entrada": entrada, "resultado": resultado})
                print(f"\nResultado: {resultado}")
            else:
                print("\nOperação inválida.\n")

        except (ValueError, IndexError):
            print("Entrada inválida. Formato correto: número operador número (ex: 4 * 2)")

    # Exibe histórico
    print("\n📜 Histórico de Cálculos:\n")
    for item in historico:
        print(f"{item['entrada']} = {item['resultado']}\n")

# Executa a calculadora
calculadora()