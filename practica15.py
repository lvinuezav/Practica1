L = [i for i in range (1,10) if i%2 == 0]

print (L)

lista = ["Frank","Carlos","Lourdes","Ana","Mercedes","Maria","Maria Belén","Fernado"]
lista_2 = [nombre.upper() for nombre in lista if nombre.lower().startswith("m")]
print(lista_2)