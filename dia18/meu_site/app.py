from flask import Flask, render_template

app = Flask(__name__)

# Rota principal, que renderiza um template HTML
@app.route('/')
def index():
    # Passando uma variável para o template
    return render_template('index.html', titulo="Bem-vindo!", nome="Desenvolvedor Python")

if __name__ == '__main__':
    app.run(debug=True)