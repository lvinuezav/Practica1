from practica34.usuario.Usuario import Usuario
from sqlalchemy.orm import sessionmaker
from practica34.base.creacionBaseDatos import engine


Session = sessionmaker(bind=engine)
session = Session()

usuario1 = Usuario()
usuario1.usuario = "cmaloxxxx"
usuario1.nombres = "Carloscccccccc"
usuario1.apellidos = "malo"
usuario1.contrasenia = "654123"

session.add(usuario1)
session.commit()

