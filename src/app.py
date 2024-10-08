from flask import Flask, url_for, request, jsonify

app = Flask(__name__)

@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
    return jsonify(
        {
            "Usuário": usuario,
            "Idade": idade,
            "Altura": altura
        }
    )
    


@app.route("/bemvindo")
def bem_vindo():
    return "<h1>Bem, vindo!</h1>"

@app.route("/projects/")
def projects():
    return "The project page"

@app.route("/about", methods=["GET","POST"])
def about():
    if request.method == 'GET':
        return 'This is a GET'
    else:
        return 'This is a POST'
    return "The about page"


with app.test_request_context():
    print(url_for('bem_vindo'))
    print(url_for('projects'))
    print(url_for('about', next='/'))
    print(url_for('hello_world', usuario='Christopher', idade=23, altura=1.84))
   