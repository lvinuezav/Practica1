import psycopg2

def conectar (usuario='postgres',password='xlqlo123*',puerto='5432',nombre_base='sismos',host='localhost'):
    db  = psycopg2.connect(database=nombre_base,user=usuario,password=password, host=host,port=puerto)
    print("Connected\n")
    return db

def leer_registro(db, tabla):
    sql = "select * from %s" % tabla
    cursor = db.cursor()
    cursor.execute(sql)
    registros = cursor.fetchall()
    return registros

def insertar_registro(tabla, datos, db):
    campos = datos.keys()
    valores = datos.values()
    sql = "INSERT INTO %s(%s) VALUES (%s);" % (tabla, ",".join(campos), "'" + "','".join(valores) + "'")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()

db = conectar()

nombre = input("Ingrese Nombre. ")
usuario = input("Ingrese Usuario: ")
insertar_registro("usuario",(usuario,nombre),db)
filas = leer_registro(db,usuario)

filas = leer_registro(db,"usuario")
for fila in filas:
    print(fila[0])
    print(fila[1])

