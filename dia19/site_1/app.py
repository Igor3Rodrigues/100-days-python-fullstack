from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo="Página Inicial")

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo="Sobre Nós")

if __name__ == "__main__":
    app.run(debug=True)