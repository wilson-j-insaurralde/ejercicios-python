# Crear y cargar una lista con 5 enteros por teclado. 
# Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra.

list = []

x = 0
for j in range(5):
    valor =int(input("ingrese valor : "))
    list.append(list)

menor = list[0]

for x in range (1,5): 
    if list[x] < menor :
        menor = list[x]
        posicion = x
print("lista :", list)
print ("menor", menor)
print("posicion: ", posicion)






