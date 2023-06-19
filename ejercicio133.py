#Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10. Desde el bloque principal del programa llamar a ambas funciones.



def cargaLista():
    lista=[]
    for j in range(5):
        val=int(input("ingrese valor entero: "))
        lista.append(val)
    print(lista)    
    return lista
def mayores(lista):
    print("elementos que son mayores a 10 de la lista: ")
    
    for j in range (len(lista)):
        if lista[j]>10:
            print(lista[j])
        

ver=cargaLista()
mayores(ver)
