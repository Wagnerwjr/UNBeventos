#Arquivo pra criar as interações com o banco de dados i.e. Criar eventos novos, favoritar/desfavoritar eventos, criar os eventos iniciais do site.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db import Evento, Favoritos, Usuario
import json


Base = declarative_base()

engine = create_engine('mysql://root:admin@127.0.0.1:3306/UNBeventos')

Session = sessionmaker(bind=engine)

session = Session()

def buscar_evento(id):
    evento_objeto = session.query(Evento.id, Evento.nome, Evento.imagem, Evento.data, Evento.hora, Evento.local, Evento.resumo).filter(Evento.id == id).first()
    evento_json = []
    evento_json.append({"id": evento_objeto[0], "nome": evento_objeto[1], "imagem": evento_objeto[2], 
                         "data": evento_objeto[3], "hora": evento_objeto[4], "local": evento_objeto[5], "resumo": evento_objeto[6]})
    evento_json = json.dumps(evento_json)

    return evento_json

def buscar_usuario(id):
    usuario_objeto = session.query(Usuario.id, Usuario.nome, Usuario.matricula, Usuario.curso, Usuario.email, Usuario.foto, Usuario.favoritos).filter(Usuario.id == id).first()
    usuario_json = []
    usuario_json.append({"id": usuario_objeto[0], "nome": usuario_objeto[1], })
    usuario_json = json.dumps(usuario_json)

    return usuario_json


def novo_evento(titulo, data, horario, local, categorias, descricao, nome, email, telefone):
    evento = Evento()


# def adicionar_usuario(id, nome, matricula, curso, email, foto, id_favorito):
#     favorito = session.query(Favoritos).filter_by(id == id_favorito).first()
#     user = Usuario(id = id, nome = nome, matricula = matricula, curso = curso, email = email, foto = foto , favoritos = favorito)
    
#     session.add(user)
#     session.commit()
    
    
    
# adicionar_usuario(1, 'Wagner',  '200044494','Ciencia da computação', '200044494@aluno.unb.br',"00000000" , 1)