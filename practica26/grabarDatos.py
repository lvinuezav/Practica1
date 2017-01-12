import practica26.earthquake.datos.geojson as g
from practica26.earthquake.bd.nosql.firebasedb import grabarEvento,leerEventos,eliminarEvento,actualizarEvento

#from practica26.earthquake.bd.nosql.firebasedb import grabarEvento
#
#g.preparar_url(starttime="2016-04-15", endtime="2016-04-30",
#             orderby = "magnitude", limit = "20")
#
#base = g.realizar_requerimiento()
#
#for evento in base["features"]:
#    grabarEvento(evento)



id='us10005cc4'
actualizarEvento(id,{"lugar":"Ecuador, guayaquil, centro"})
