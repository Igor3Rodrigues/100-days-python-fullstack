from flask import Flask, render_template

app = Flask(__name__)

# Simulação de posts (em breve virão de um banco de dados)
posts = [
    {"id": 1, "titulo": "Primeiro Post", "conteudo": "Este é o conteúdo do primeiro post."},
    {"id": 2, "titulo": "Segundo Post", "conteudo": "Este é o conteúdo do segundo post."}
]

@app.route('/')
def homepage():
    # Passa os posts para o template
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)