# Classe base (superclasse)
class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
    
    # Método comum a todos os animais
    def emitir_som(self):
        print(f"{self.nome} faz um som.")
        
    # Exibir dados básicos
    def exibir_info(self):
        print(f"\nNome: {self.nome}")
        print(f"Espécie: {self.especie}")
    
# Classe derivada (subclasse)
class Cachorro(Animal):
    def __init__(self, nome, raca):
        # Chama o construtor da superclasse Animal
        super().__init__(nome, raca)
        self.raca = raca
    
    # Método específico da subclasse
    def latir(self):
        print(f"{self.nome} está latindo: Au Au!\n")
        
    # Sobrescrita (override) de método da superclasse
    def emitir_som(self):
        self.latir()
        
# Criando um objeto da classe Cachorro
dog = Cachorro("Bolt", "Golden Retriever")

# Usando métodos herdados e específicos
dog.exibir_info() # Método herdado
dog.emitir_som()  # Método sobrescrito
