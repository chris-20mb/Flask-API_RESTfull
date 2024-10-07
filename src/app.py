from flask import Flask, url_for

app = Flask(__name__)

@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
    print(idade)
    print(f"tipo da variável idade: {type(idade)}")
    print(f"tipo da variável usuário: {type(usuario)}")
    print(f"tipo da variável altura: {type(altura)}")
    return f"<h1>Olá mundo! usuário: {usuario.upper()}</h1>"
    


@app.route("/bemvindo")
def bem_vindo():
    return "<h1>Bem, vindo!</h1>"

@app.route("/projects/")
def projects():
    return "The project page"

@app.route("/about")
def about():
    return "The about page"


with app.test_request_context():
    print(url_for('bem_vindo'))
    print(url_for('projects'))
    print(url_for('about', next='/'))
   