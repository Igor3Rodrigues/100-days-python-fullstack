from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        
        if nome and email:
            message = f"Olá, {nome}! Seu e-mail {email} foi recebido com sucesso."
        else:
            message = "Por favor, preencha todos os campos."
    
    return render_template('form.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)