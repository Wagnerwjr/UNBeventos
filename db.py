from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date, time
from route import app

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



