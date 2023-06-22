from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='C:/Users/Wagner/UNBeventos/templates')
app._static_folder = 'C:/Users/Wagner/UNBeventos/static'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@127.0.0.1:3306/UNBeventos'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)


with app.app_context():
    db.create_all()





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