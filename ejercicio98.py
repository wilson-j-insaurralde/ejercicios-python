#Se tiene la siguiente lista:
#lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
#Imprimir la lista. Luego fijar con el valor cero todos los elementos mayores a 50 del primer elemento de 
#"lista".
#Volver a imprimir la lista.

lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
x=0
for k in range (len(lista)):
    for x in range (len(lista[k])):
        print(lista[k][x])


for k in range (len(lista)):
    for x in range(len(lista[k])):
        if lista [k][0]>50:
            lista[k][0]=0

print(lista)



