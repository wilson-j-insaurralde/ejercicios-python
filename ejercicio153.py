# Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un pais y la cantidad de habitantes.
#Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla y en la tercera mostrar el nombre del país con mayor cantidad de habitantes.

def pais():
    pais=[]
    for j in range(5):
        nom=input("ingrese nombre del pais: ")
        cant=float(input("ingrese cantidad de habitantes: "))
        pais.append((nom,cant))
    return pais 

def imprimir(pais):
    print("paises y supoblacion")
    for j in range (5):
        print(pais[j][0],pais[j][1])
    return 

def mayor(pais):
    mayor=0
    for j in range (1,5):
        if pais[j][1]>pais[mayor][1]:
            mayor=j
    print ("el pais con mayor poblacion es:",pais[mayor][0])

pais= pais()
imprimir(pais)
mayor(pais)



