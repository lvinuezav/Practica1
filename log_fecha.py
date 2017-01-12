import datetime

f = open("log.txt", "a")
fecha_actual = datetime.datetime.today().strftime("%d-$s-%Y %H:%M:%S")
f.write(fecha_actual)