# Crear y cargar una lista con 5 enteros. Implementar un algoritmo que identifique el mayor valor de la lista.

list = []
x = 0 
for j in range (5):
    ele = int(input("ingrese entero: "))
    list.append(ele)
 
mayor = list[0]

for x  in range (1,5):
    if list[x] > mayor :
        mayor = list[x]
print (mayor)