#Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. Implementar una función que imprima el mayor y el menor valor de la lista.


def mayor(x):
    mayor=x[0]
    for j in range(1,len(x)):
        if x[j]>mayor:
            mayor= x[j]
    return mayor
def menor(x):
    menor=x[0]
    for j in range(1,len(x)):
        if x[j]<menor:
            menor= x[j]
    return menor
lista=[]
for j in range (5):
    va=int(input("ingrese valor entero: "))
    lista.append(va)

print ("la lista es:",lista)
print("el mayor es: ",mayor(lista))
print("el menor es: ", menor(lista))

