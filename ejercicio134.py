# Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista. Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.

def lista():
    lista=[]
    for j in range (5):
        val=int(input("ingrese valor entero: "))
        lista.append(val)
        
    print(lista)
    return lista

def mayor(lista):
    mayor=lista[0]
    for x in range (1,5):
        if lista[x]>mayor:
            mayor=lista[x]
    print("el mayor es: ",mayor)
    return mayor
def menor (lista):
    menor=lista[0]
    for x in range(1,5):
        if lista[x]<menor:
            menor=lista[x]
    print("el menor es: ",menor)
    return menor

val=lista()
mayor(val)
menor(val)
