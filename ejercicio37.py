# Realizar un programa que permita cargar dos listas de 15 valores cada una.
# Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor
# (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
#Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

cont1 = 0
cont2 = 0
cont3 = 1
print("carga de la primera lista ")
while cont3 <= 15:
    list1 = float (input("ingrese valor de la lista 1: "))
    cont1 = cont1 + list1 
    cont3 = cont3 + 1 

cont3 = 1    
print("carga de la segunda lista ")
while cont3 <= 15:
    list2 = float (input("ingrese valor de la lista 2: "))
    cont2 = cont2 + list2 
    cont3 = cont3 + 1 


if cont1 == cont2:
    print("lista iguales ")
else:
    if list1 > list2 :
        print("lista 1 mayor")
    else:
        print("lista 2 mayor")
