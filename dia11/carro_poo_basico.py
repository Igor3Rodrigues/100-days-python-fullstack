# Definindo a classe Carro
class Carro:
    def __init__(self, modelo, cor, ano):
        # Atributos da classe
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        
    # Método para exibir as informações do carro
    def exibir_detalhes(self):
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Ano: {self.ano}")
    
    # Método para simular ligar o carro
    def ligar(self):
        print(f"O {self.modelo} está ligado")
        
    # Método para simular desligar o carro
    def desligar(self):
        print(f"O {self.modelo} está desligado")

# Criando objetos (instâncias) da classe Carro
meu_carro = Carro("Civic", "Prata", 2022)
carro_amigo = Carro("Gol", "Vermelho", 2015)

# Usando os métodos da classe
print("Informações do meu carro:")
meu_carro.exibir_detalhes()
meu_carro.ligar()

print("\nInformações do carro do amigo:")
carro_amigo.exibir_detalhes()
carro_amigo.desligar()