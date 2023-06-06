#Solicitar por teclado dos enteros. El primer valor indica la cantidad de elementos que crearemos en la lista.
#El segundo valor indica la cantidad de elementos que tendrá cada una de las listas internas a la lista principal.
#Mostrar la lista y la suma de todos sus elementos.

#Por ejemplo si el operador carga un 2 y un 4 significa que debemos crear una lista similar a:

#lista=[[1,1,1,1], [1,1,1,1]]


x= int(input("ingrese cantidad de elementos: "))
y= int (input("ingrese cantidad de elemntos de la lista interna: "))
lista= []

for k in range(x):
    lista.append([])
    for j in range(y):
        valor = int(input("ingrese numero: "))
        lista[k].append(valor)
print(lista)    

suma=0 

for j in range(len(lista)):
    for z in range (len(lista[j])):
        suma=suma + lista[j][z]


print("La suma de todos sus elementos:",suma)  

