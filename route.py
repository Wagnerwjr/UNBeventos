from flask import Flask, render_template, request
from interactions import  buscar_usuario, novo_evento
import base64

app = Flask(__name__, template_folder='C:/Users/Wagner/UNBeventos/templates')
app._static_folder = 'C:/Users/Wagner/UNBeventos/static'
# app = Flask(__name__, template_folder='C:/Users/wagner.junior/UNBeventos/templates')
# app._static_folder = 'C:/Users/wagner.junior/UNBeventos/static'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@127.0.0.1:3306/UNBeventos'

#Pagina inicial
@app.route("/", methods = ['GET', 'POST'])
def homepage():
    return render_template("homepage.html")


@app.route('/cadastrar')
def cadatrar_dados():
    return render_template('Cadastro de Evento.html')

@app.route('/cadastrar-dados', methods = ['POST'])
def cadastrar_evento():
    titulo = request.form['titulo']
    data = request.form['data']
    horario = request.form['horario']
    local = request.form['local']
    categorias = request.form['categorias']
    descricao = request.form['descricao']
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    imagem = request.files.get('myFile')
    
    if imagem is not None:
        imagem_bin = imagem.read()
        
    else:
        imagem_bin = 0

    print(titulo, data, horario, local, categorias, descricao, nome, email, telefone, imagem_bin)
    novo_evento(titulo, data, horario, local, categorias, descricao, nome, email, telefone, imagem)
    return confirmar_evento()
# @app.route('/evento/<id>')
# def cadastrar_evento(id):
#     ### buscar no banco id do evento
#     conteudo = buscar_evento(id)
#     return render_template('cadastro.html', conteudo = conteudo)

@app.route('/usuario/<id>')
def perfil_usuario(id):
    ### buscar no banco id do usuario
    conteudo = buscar_usuario(id)
    return render_template('Perfil do Usuario.html', conteudo = conteudo)

@app.route('/confirmacao-evento')
def confirmar_evento():
    return render_template("Confirmacao de Evento Cadastrado.html")

@app.route('/confirmacao-inscricao')
def confirmar_inscricao():
    return render_template("Confirmacao de Inscricao.html")



# @app.route('/favoritos/<id>')
# def confirmar_evento(id):

#     return render_template("favoritos.html")

app.run()
