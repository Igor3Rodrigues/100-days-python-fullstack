from flask import Flask, render_template

app = Flask(__name__)

# Lista de posts mockados (simulados)
posts = [
    {"id": 1, "titulo": "Python para Iniciantes", "conteudo": "Aprenda o básico de Python.", "autor": "Maria"},
    {"id": 2, "titulo": "Flask em 5 minutos", "conteudo": "Um guia rápido para Flask.", "autor": "João"},
    {"id": 3, "titulo": "100 Dias de Código", "conteudo": "Como manter uma rotina de estudos?", "autor": "Ana"}
]

@app.route('/')
def homepage():
    # Envia a lista de posts para o template
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)