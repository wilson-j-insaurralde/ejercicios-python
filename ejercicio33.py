# Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.
n = int(input("numero de personas: "))
x = 1
suma = 0

while x <= n :
    altura = float(input("ingrese altura:"))
    suma = suma + altura 
    x = x + 1 
promedio = suma /n

print("la altura promedio es de ", promedio)
