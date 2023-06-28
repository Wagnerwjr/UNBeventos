#Arquivo pra criar as interações com o banco de dados i.e. Criar eventos novos, favoritar/desfavoritar eventos, criar os eventos iniciais do site.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db import Evento
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