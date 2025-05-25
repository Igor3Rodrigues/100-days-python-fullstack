from flask import Flask, render_template, abort

app = Flask(__name__)

posts = [
    {"id": 1, "titulo": "Python para Iniciantes", "conteudo": "Aprenda o básico de Python.", "autor": "Maria"},
    {"id": 2, "titulo": "Flask em 5 minutos", "conteudo": "Um guia rápido para Flask.", "autor": "João"},
    {"id": 3, "titulo": "100 Dias de Código", "conteudo": "Como manter uma rotina de estudos?", "autor": "Ana"}
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:id>')
def exibir_post(id):
    for post in posts:
        if post["id"] == id:
            return render_template('post.html', post=post)
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)
