import requests
import threading
import time

def obtenerDatosAArchivo(nombre_archivo, fecha_inicial, fecha_final, id_proceso):
    url = 'http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=%s&endtime=%s' % (fecha_inicial, fecha_final)
    response = requests.get(url)
    data = response.text
    f = open(nombre_archivo, "a")
    eventos = data.split("\n")
    for indice in range(len(eventos)):
        if indice > 0:
            evento = eventos[indice]
            datos = evento.split("|")
            if len(datos) == 13 :
                if datos[10]:
                    magnitud = datos[10]
                    lugar = datos[12]
                    linea = "%d magnitud: %s, lugar: %s \n" % (id_proceso, magnitud, lugar)
                    f.write(linea)
                    print("Escribiendo: %d" %id_proceso)
                    time.sleep(0.25)
    f.close()


# obtenerDatosAArchivo("sismo.txt", "2016-01-01", "2016-02-01")
# obtenerDatosAArchivo("sismo.txt", "2016-02-02", "2016-03-01")
# obtenerDatosAArchivo("sismo.txt", "2016-03-02", "2016-04-01")

lista_procesos = []
lista_procesos.append(threading.Thread(target=obtenerDatosAArchivo, args=("sismo.txt", "2016-01-01", "2016-02-01", 1)))
lista_procesos.append(threading.Thread(target=obtenerDatosAArchivo, args=("sismo.txt", "2016-02-02", "2016-03-01", 2)))
lista_procesos.append(threading.Thread(target=obtenerDatosAArchivo, args=("sismo.txt", "2016-03-02", "2016-04-01", 3)))
lista_procesos.append(threading.Thread(target=obtenerDatosAArchivo, args=("sismo.txt", "2016-04-02", "2016-05-01", 4)))
lista_procesos.append(threading.Thread(target=obtenerDatosAArchivo, args=("sismo.txt", "2016-05-02", "2016-06-01", 5)))
lista_procesos.append(threading.Thread(target=obtenerDatosAArchivo, args=("sismo.txt", "2016-06-02", "2016-07-01", 6)))

for t in lista_procesos:
    t.start()

# t = threading.Thread(target=obtener_sismos)
# t.start()