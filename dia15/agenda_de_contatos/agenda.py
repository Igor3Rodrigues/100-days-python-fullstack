from contato import Contato

# Classe para gerenciar a lista de contatos
class Agenda:
    def __init__(self):
        self.contatos = []
        
    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        
    def listar_contatos(self):
        if not self.contatos:
            print("Agenda vazia.")
        for i, contato in enumerate(self.contatos):
            print(f"\nContato {i + 1}")
            contato.exibir()
            
    def editar_contato(self, indice, nome=None, telefone=None, email=None):
        if 0 <= indice < len(self.contatos):
            self.contatos[indice].editar(nome, telefone, email)
        else:
            print("Índice inválido.")
    
    def excluir_contato(self, indice):
        if 0 <= indice < len(self.contatos):
            del self.contatos[indice]
        else:
            print("Índice inválido.")