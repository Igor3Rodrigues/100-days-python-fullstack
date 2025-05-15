# Arquivo: models/historico.py

class Historico:
    def __init__(self):
        self.operacoes = []
        
    def adicionar(self, operacao_str):
        self.operacoes.append(operacao_str)
        
    def salvar_em_arquivo(self, caminho):
        with open(caminho, 'a', encoding='utf-8') as arquivo:
            for operacao in self.operacoes:
                arquivo.write(operacao+ '\n')
                
    def mostrar(self):
        for op in self.operacoes:
            print(op)