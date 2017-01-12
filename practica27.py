import threading, requests

def obtener_sismos():
    response = requests.get(
        "http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-16&endtime=2016-06-05")
    data = response.text

    eventos = data.split("\n")
    for indice in range(len(eventos)):
        if indice > 0:
            evento = eventos[indice]
            datos = evento.split("|")
            if len(datos) == 13 and datos[12].lower().find("ecuador"):
                if datos[10]:
                    magnitud = float(datos[10])
                    print ({"value":magnitud})

#obtener_sismos()
t = threading.Thread(target=obtener_sismos)
t.start()
print("test")