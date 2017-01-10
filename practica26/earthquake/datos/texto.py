import requests
from practica26.earthquake.datos.constantes import URL_BASE

def validar_magnitud(func):
    def envoltura(evento):
        datos = func(evento)
        if len(datos)!= 13 or datos[10] == '':
            return None
        else:
            return datos
    return envoltura

def preparar_url(format = "text", **kwargs):
    global URL_BASE

    URL_BASE += "?format=%s"%format
    argumentos = ""
    for k,v in kwargs.items():
        argumentos += "&%s=%s" % (k,v)
        URL_BASE += argumentos

def realizar_requerimiento():
    response = requests.get(URL_BASE)
    return response.text

def obtener_eventos(base_completa, q=None):
    eventos = base_completa.split("\n")
    resultado = []
    count = 0
    for evento in eventos:
        if q is not None:
            if evento.lower().find(q.lower()) >= 0:
                resultado.append(evento)
        else:
            if count != 0:
                resultado.append(evento)
            count += 1
    return resultado

@validar_magnitud
def obtener_datos(evento):
    return evento.split("|")
