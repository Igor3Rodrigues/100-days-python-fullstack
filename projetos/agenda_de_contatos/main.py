from agenda import Agenda
from contato import Contato

# Função principal para rodar o menu
def menu():
    agenda = Agenda()
    while True:
        print("\n--- MENU ---")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Editar contato")
        print("4. Excluir contato")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            contato = Contato(nome, telefone, email)
            agenda.adicionar_contato(contato)
        elif escolha == '2':
            agenda.listar_contatos()
        elif escolha == '3':
            indice = int(input("Número do contato para editar: ")) - 1
            nome = input("Novo nome (pressione Enter para manter): ")
            telefone = input("Novo telefone (pressione Enter para manter): ")
            email = input("Novo email (pressione Enter para manter): ")
            agenda.editar_contato(indice, nome or None, telefone or None, email or None)
        elif escolha == '4':
            indice = int(input("Número do contato para excluir: ")) - 1
            agenda.excluir_contato(indice)
        elif escolha == '5':
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    menu()
