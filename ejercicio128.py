#Definir por asignación una lista de enteros en el bloque principal del programa. Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus elementos, la segunda recibe la lista y retorna el mayor valor y la última recibe la lista y retorna el menor.

def listSuma(x):
    suma=0
    for j in range (len(x)):
        suma=suma + x[j]
    return suma 
def listMayor(x):
    mayor=x[0]
    for j in range (1,len(x)):
        if x[j]> mayor:
            mayor= x[j]
    return mayor
def listaMenor(x):
    menor= x[0]
    for j in range (1,len(x)):
        if x[j]<menor:
            menor = x[j]
    return menor 

listavalores=[10, 56, 23, 120, 94]
print("La lista completa es")
print(listavalores)
print("La suma de todos su elementos es", listSuma(listavalores))
print("El mayor valor de la lista es", listMayor(listavalores))
print("El menor valor de la lista es", listaMenor(listavalores))

