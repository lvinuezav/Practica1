def suma(a,b):
    return a+b

def imprimir_resultado(valor):
    print("El resultado es", valor)

x = 5
y = 15

imprimir_resultado (suma(x,y))

######################################################################################################

def suma(a,b):
    return a+b

def imprimir_resultado(valor = ""):
    if not valor:
        print("No hay resultado")
    else:
        print("El resultado es:", valor)
x = 5
y = -15

imprimir_resultado (suma(a=y,b=x))
imprimir_resultado ()