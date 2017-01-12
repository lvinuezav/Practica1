import pyrebase

DB_URL = "https://practica26-7e4d4.firebaseio.com/users/Morty"
CONTENEDOR ="sismos"

config = {
  "apiKey": "AIzaSyARFfd7TGS4RfZLCECzD3tPqsinacAcxDI",
  "authDomain": "practica26-7e4d4.firebaseapp.com",
  "databaseURL": "https://practica26-7e4d4.firebaseio.com",
  "storageBucket": "practica26-7e4d4.appspot.com"
}

firebase = pyrebase.initialize_app(config)

def obtenerBaseDatos():
    #auth = firebase.auth()
    #user = auth.sign_in_with_email_and_password("frankmalo86@gmail.com", "p.123456")
    db = firebase.database()
    return db


def grabarEvento(evento):
    registro = {"magnitud":11, "lugar": evento["properties"]["place"],
                "tiempo": evento["properties"]["time"], "longitud":evento["geometry"]["coordinates"][0],
                "latitud":evento["geometry"]["coordinates"][1]}
    db = obtenerBaseDatos()
    results = db.child(CONTENEDOR).child(evento["id"]).set(registro)

def leerEventos():
    db = obtenerBaseDatos()
    return db.child("sismos").order_by_child("tiempo").get()

def eliminarEvento(id):
    db = obtenerBaseDatos()
    return db.child("sismos").child(id).remove()


def actualizarEvento(id, campo_actualizar): #id que voy a actualizar
    db = obtenerBaseDatos()
    db.child("sismos").child(id).update(campo_actualizar)