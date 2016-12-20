import requests
import time
import datetime


response = requests.get('http://earthquake.usgs.gov/fdsnws/event/1/query?format=text&starttime=2016-04-16&endtime=2016-05-20')
data = response.text


from ubidots import ApiClient

api = ApiClient(token='aw3vYXYy13i9xVl75Zt1jQAsQpde8j')
my_variable = api.get_variable('5848c8d47625422c4ec9767e')


eventos = data.split("\n")
eventos.reverse()
for indice in range(len(eventos)):
    if indice > 0:
        evento = eventos[indice]
        datos = evento.split("|")
        if len(datos) == 13 and  datos[12].lower().find("ecuador") >0:
            if datos[10]:
                fecha_str = datos[1]
                fecha_str = fecha_str[:fecha_str.index(".")]
                fecha_timestamp = time.mktime(datetime.datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M:%S").timetuple())
                fecha_timestamp -= (5*60*60)
                #print (fecha_timestamp)
                magnitud = float(datos[10])
                lat = float(datos[2])
                lon = float(datos[3])
                new_value = my_variable.save_value({'value': magnitud, 'timestamp': int(fecha_timestamp * 1e3), "context":{"lat":lat, "lng":lon}})
                time.sleep(2)