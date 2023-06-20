#Cargar una lista de 10 enteros, luego mostrarlos por pantalla a cada elemento separados por una coma.

def listaEntero():
    lista=[]
    for j in range (10):
        val=int(input("ingrese valor entero: "))
        lista.append(val)

    return lista

def imprimir(lista):
    for j in range (10):
        print(lista[j],end=",")

lista=listaEntero()
imprimir(lista)

