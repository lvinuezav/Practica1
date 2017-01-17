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
    valores_list = []
    for valor in valores:
        if type(valor) in (float, int):
            valores_list.append(str(valor))
        elif type(valor) in (str,):
            valores_list.append("'" + valor + "'")
    sql = "INSERT INTO %s(%s) VALUES (%s);" % (tabla, ",".join(campos), ",".join(valores_list))
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()


db = conectar()
op = -1
while op != 0:
    nombre = input("Ingrese el nombre: ")
    usuario = input("iIngrese el usuario: ")
    edad = int(input("iIngrese el usuario: "))
    datos = {"nombre":nombre, "usuario":usuario, "edad":edad}
    insertar_registro("usuario", datos , db)
    filas = leer_registro(db, "usuario")
    for fila in filas:
        print(fila[0])
        print(fila[1])
        print(fila[2])
        print(fila[3])
        print("################################################")
    op = int(input("Ingrese la opcion: "))
db.close()








    #     cursor = conn.cursor()
    #     print ("Connected!\n")