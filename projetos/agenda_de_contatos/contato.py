# Classe que representa um contato
class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        
    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.email}")
        
    def editar(self, nome=None, telefone=None, email=None):
        if nome:
            self.nome = nome
        if telefone:
            self.telefone = telefone
        if email:
            self.email = email