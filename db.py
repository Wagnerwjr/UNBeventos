import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, text, Column, Integer, String, DateTime, Numeric, update, inspect, insert,MetaData, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine('mysql://root:admin@127.0.0.1:3306/UNBeventos')

Session = sessionmaker(bind=engine)

session = Session()
app = flask.Flask(__name__, template_folder='C:/Users/Wagner/UNBeventos/templates')
app._static_folder = 'C:/Users/Wagner/UNBeventos/static'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@127.0.0.1:3306/UNBeventos'

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

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
    nome = db.Column(db.String(80), nullable=False)
    imagem  = db.Column(db.LargeBinary, nullable=True)
    data = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time(80) ,nullable=False)
    local = db.Column(db.String(80), nullable=False)
    resumo = db.Column(db.String(1000), nullable=True)
    organizadores = relationship("Organizadores", secondary=association_table_organizadores, back_populates="eventos")
    categorias = relationship("Categorias", secondary=association_table_categorias, back_populates="eventos")

class Organizadores(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(80), nullable=False)
    eventos = relationship("Evento", secondary=association_table_organizadores, back_populates="organizadores")

class Categorias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    eventos = relationship("Evento", secondary=association_table_categorias, back_populates="categorias")

class Favoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.id'), nullable=False)
    evento = db.relationship('Evento', backref='favoritos')

class EventosCriados(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.id'), nullable=False)
    evento = db.relationship('Evento', backref='criados')

