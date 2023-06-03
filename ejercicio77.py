# Almacenar en una lista los sueldos (valores float) de 5 operarios.
# Imprimir la lista y el promedio de sueldos
import math
list = []
suma = 0

for f in range (5):
    valor = float(input("ingrese sueldo:"))
    list.append(valor)
    suma = suma + valor 

print (list)

print("promedio: ",(suma / 5))    