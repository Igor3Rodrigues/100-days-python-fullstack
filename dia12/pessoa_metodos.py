# Definindo a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    # Método para exibir os dados da pessoa
    def exibir_informacoes(self):
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade} anos\n")
        
    # Método para alterar o nome
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        print(f"Nome atualizado com sucesso!")
        
    # Método para alterar a idade
    def alterar_idade(self, nova_idade):
        if nova_idade > 0:
            self.idade = nova_idade
            print(f"Idade atualizada com sucesso!")
        else:
            print("Idade inválida.")

# Criando um objeto do tipo Pessoa
p1 = Pessoa("Igor", 27)

# Exibindo as informações iniciais
p1.exibir_informacoes()

# Alterando o nome e a idade da pessoa
p1.alterar_nome("Igor Rodrigues")
p1.alterar_idade(28)

# Exibindo novamente após alterações
print("\nApós alterações:")
p1.exibir_informacoes()