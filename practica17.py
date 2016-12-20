#####################################################################################

#pip install spotipy

#####################################################################################

##presentar los resultados
##ordenar (de acuerdo a cualquier criterio,
#el usuario elija)
#convertir tiempo ms en string h:m:s
#crear una lista de favoritos


#####################################################################################


from spotify import buscar_musica
import time

menu1 = """
1.- ordenar los resultados
2.- agregar a favoritos
3.- buscar
4.- presentar resultados
5.- presentar favoritos
6.- salir

"""

menu2 = """
1.- Ordenar por track
2.- Ordenar por popularidad
3.- Ordenar por tiempo

"""

menu3="""
Ingrese el número de resultado que desea agregar a favoritos:

"""
resultados = []
favoritos = []
opcion = 0

while opcion != 6:
    opcion = int(input(menu1))

    if opcion == 1:
        if resultados:
            ordenamiento = int(input(menu2))
            if ordenamiento == 1:
                resultados.sort(key=lambda x: x[0])
            elif ordenamiento == 2:
                resultados.sort(key=lambda x: x[1], reverse=True)
            elif ordenamiento == 3:
                resultados.sort(key=lambda x: x[3], reverse=True)
            else:
                print("opcion incorrecta")
        else:
            print("Primero realice una busqueda")
    elif opcion == 2:
        if resultados:
            opcion_favorito = int(input(menu3))
            if opcion_favorito < len(resultados):
                favoritos.append(resultados[opcion_favorito - 1])
            else:
                print("El indice se encuentra fuera de los limites")
        else:
            print("Primero realice una busqueda")
    elif opcion == 3:
        q = input("Ingrese el criterio de busqueda: ")
        resultados = buscar_musica(q, 30)
    elif opcion == 4:
        if resultados:
            for resultado in resultados:
                print("Track \t %s" % resultado[0])
                print("Popularidad \t %d" % resultado[1])
                print("Preview \t %s" % resultado[2])
                print("Duración \t %s" % time.strftime("%H:%M:%S", time.gmtime(resultado[3] / 1e3)))
                print("Autor \t %s" % resultado[4])
                print("")
    elif opcion == 5:
        if favoritos:
            for resultado in favoritos:
                print("Track \t %s" % resultado[0])
                print("Popularidad \t %d" % resultado[1])
                print("Preview \t %s" % resultado[2])
                print("Duración \t %s" % time.strftime("%H:%M:%S", time.gmtime(resultado[3] / 1e3)))
                print("Autor \t %s" % resultado[4])
                print("")