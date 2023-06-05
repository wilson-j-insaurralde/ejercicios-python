# Cargar una lista con 5 elementos enteros. Ordenarla de menor a mayor y mostrarla por pantalla,
# luego ordenar de mayor a menor e imprimir nuevamente.

list = []

aux = 0

for j in range (5): 
    valor = int(input("ingrese valor: "))
    list.append(valor)

for j in range (4):
    for p in range (4):
        if list[p]>list[p+1]:
            aux=list[p+1]
            list[p+1]=list[p]
            list[p]= aux

print("lista ordenada de mayor a menor: ", list)

for j in range (4):
    for p in range (4):
        if list[p]<list[p+1]:
            aux=list[p+1]
            list[p+1]=list[p]
            list[p]= aux
print ("lista ordenada de menor a mayor:", list)