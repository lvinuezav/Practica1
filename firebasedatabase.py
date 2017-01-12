import pyrebase

DB_URL = "https://practica26-7e4d4.firebaseio.com/users/Morty"
CONTENEDOR ="usuarios"

config = {
  "apiKey": "AIzaSyARFfd7TGS4RfZLCECzD3tPqsinacAcxDI",
  "authDomain": "practica26-7e4d4.firebaseapp.com",
  "databaseURL": "https://practica26-7e4d4.firebaseio.com",
  "storageBucket": "practica26-7e4d4.appspot.com"
}

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password("lvinueza@eas.ec", "123***")

# Get a reference to the database service
db = firebase.database()

# data to save
data = {
    "name": "Ana Vacacela", "edad":"76", "correo":None,"colores":"rojo"
}

# Pass the user's idToken to the push method
#results = db.child("users").push(data, user['idToken'])
#db.child("users").child("0919806083").set(data)
results = db.child(CONTENEDOR).child("0919806083").set(data)