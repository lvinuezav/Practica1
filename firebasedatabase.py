import pyrebase

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
    "name": "Mortimer 'Morty' Smith", "correo":"lvinueza@eas.ec", "colores":"rojo"
}

# Pass the user's idToken to the push method
#results = db.child("users").push(data, user['idToken'])
db.child("users").child("Morty").set(data)