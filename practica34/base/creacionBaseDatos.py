from sqlalchemy import create_engine
from practica34.base import base
from practica34.usuario.Usuario import Usuario

engine = create_engine('postgresql://postgres:postgres@localhost:5433/practica34')
base.Base.metadata.create_all(engine)