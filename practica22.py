d = {1:"test",1.1:[5,7,"otro test"],"tercer":"otra cadena",(1,0):5, (5,4):1.1}

print (d[1])
print (d[1.1])
print (d["tercer"])
print (d[1,0])

d[3] = "Nuevo elemento"
d[1] = "Remplazo de Valor"

print (d)

del d[1.1]
print (d)