from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date, time


app = Flask(__name__, template_folder='C:/Users/Wagner/UNBeventos/templates')
app._static_folder = 'C:/Users/Wagner/UNBeventos/static'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@127.0.0.1:3306/UNBeventos'
db = SQLAlchemy(app)


association_table_organizadores = Table(
    'association_organizadores',
    db.Model.metadata,
    db.Column('evento_id', db.Integer, db.ForeignKey('evento.id')),
    db.Column('organizador_id', db.Integer, db.ForeignKey('organizadores.id'))
)

association_table_categorias = Table(
    'association_categorias',
    db.Model.metadata,
    db.Column('evento_id', db.Integer, db.ForeignKey('evento.id')),
    db.Column('categoria_id', db.Integer, db.ForeignKey('categorias.id'))
)

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80) nullable=False)
    imagem  = db.Column(db.LargeBinary nullable=True)
    data = db.Column(db.Date nullable=False)
    hora = db.Column(db.Time(80) nullable=False)
    local = db.Column(db.String(80) nullable=False)
    resumo = db.Column(db.String(1000) nullable=True)
    organizadores = relationship("Organizadores", secondary=association_table_organizadores, back_populates="eventos")
    categorias = relationship("Categorias", secondary=association_table_categorias, back_populates="eventos")

class Organizadores(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(80) nullable=False)
    eventos = relationship("Evento", secondary=association_table_organizadores, back_populates="organizadores")

class Categorias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80) nullable=False)
    eventos = relationship("Evento", secondary=association_table_categorias, back_populates="categorias")

class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.id'), nullable=False)
    evento = db.relationship('Evento', backref='favoritos')

class EventosCriados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.id'), nullable=False)
    evento = db.relationship('Evento', backref='criados')


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
