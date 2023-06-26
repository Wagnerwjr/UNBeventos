from flask import Flask, render_template, request

app = Flask(__name__, template_folder='C:/Users/Wagner/UNBeventos/templates')
app._static_folder = 'C:/Users/Wagner/UNBeventos/static'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@127.0.0.1:3306/UNBeventos'

#Pagina inicial
@app.route("/")
def homepage():
    return render_template("homepage.html", var = "teste2")


@app.route('/cadastrar-dados')
def cadatrar_dados():
    dados = request.get_json()

@app.route('/cadastrar')
def cadastrar_evento():
    return render_template('cadastro.html')

# @app.route('/evento/<id>')
# def cadastrar_evento(id):
#     ### buscar no banco id do evento
#     return render_template('cadastro.html')

# @app.route('/usuario/<id>')
# def perfil_usuario(id):
#     ### buscar no banco id do usuario
#     return render_template('usuario.html')


app.run()
