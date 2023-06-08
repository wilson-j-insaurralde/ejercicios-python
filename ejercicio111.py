# Crear una lista de 5 enteros y cargarlos por teclado. Borrar los elementos mayores o iguales a 10 y generar una nueva lista con dichos valores.

lista = []
lista2 = []

for k in range (5):
    valor= int(input("ingrese valor entero:"))
    lista.append(valor)
print(lista)
aux=0
while aux < len(lista):
    if lista[aux]<= 10:
       lista2.append(lista.pop(aux))
    else:
        aux = aux + 1 
print(lista)
print(lista2)



