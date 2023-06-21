# Confeccionar un programa con las siguientes funciones:
#1)Cargar una lista de 5 enteros.
#2)Retornar el mayor y menor valor de la lista mediante una tupla.
#Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.


def listaenteros():
    lista=[]
    for j in range (5):
        val=int(input("ingrese numero entero: "))
        lista.append(val)
    print(lista)
    return lista

def MayoryMenor(lista):
    mayor= lista [0]
    menor =lista[0]
    for j in range (1,5):
        if lista[j]>mayor:
            mayor=lista[j]
        else:
            if lista[j]<menor:
                menor = lista[j]
    return (mayor,menor)

lista = listaenteros()
mayor,menor=MayoryMenor(lista)
print("Mayor valor de la lista:",mayor)
print("Menor valor de la lists:",menor)


