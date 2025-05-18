# app.py
from flask import Flask

# Criação da aplicação Flask
app = Flask(__name__)

# Rota principal que retorna um texto
@app.route('/')
def home():
    return 'Olá! Bem-vindo ao meu primeiro app Flask'

# Execução do servidor em domo debug
if __name__ == '__main__':
    app.run(debug=True)