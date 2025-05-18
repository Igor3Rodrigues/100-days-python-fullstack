## mini_site_flask.py
from flask import Flask

app = Flask(__name__)

# Página inicial
@app.route('/')
def home():
    return 'Pagina Inicial'

# Pagina "Sobre"
@app.route('/sobre')
def sobre():
    return 'Esta é a página Sobre'

# Pagina "Contatos"
@app.route('/contato')
def contato():
    return 'Entre em contato pelo e-mail: contato@exemplo.com'

# Pagina "Serviços"
@app.route('/servicos')
def servicos():
    return 'Nossos serviços incluem desenvolvimento web, design e consultoria.'

if __name__ == '__main__':
    # Ativando o modo debug para atualizar automaticamente
    app.run(debug=True)