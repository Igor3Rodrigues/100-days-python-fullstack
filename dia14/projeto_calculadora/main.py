# Arquivo: main.py

from utils import operacoes
from models.historico import Historico

def main():
    hist = Historico()
    caminho_arquivo = "data/historico.txt"
    
    while True:
        print("\n--- Calculadora CLI ---\n")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Ver histórico")
        print("6. Sair")
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == "6":
            hist.salvar_em_arquivo(caminho_arquivo)
            print("Saindo da calculadora. Até logo!")
            break
        
        if escolha == "5":
            print("\nHistórico de operações:")
            hist.mostrar()
            continue
        
        try:
            a = float(input("\nDigite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            
            if escolha == "1":
                resultado = operacoes.somar(a, b)
                op = f"{a} + {b} = {resultado}"
            elif escolha == "2":
                resultado = operacoes.subtrair(a, b)
                op = f"{a} - {b} = {resultado}"
            elif escolha == "3":
                resultado = operacoes.multiplicar(a, b)
                op = f"{a} * {b} = {resultado}"
            elif escolha == "4":
                resultado = operacoes.dividir(a, b)
                op = f"{a} / {b} = {resultado}"
            else:
                print("Opção inválida.")
                continue
            
            print(f"Resultado: {resultado}")
            hist.adicionar(op)
            
        except ValueError as ve:
            print(f"Erro: {ve}")
        except Exception as e:
            print("Erro inesperado:", e)

if __name__ == "__main__":
    main()