"""Realizar un programa que solicite la carga de valores enteros por teclado y los sume.
 Finalizar la carga al ingresar el valor -1. Dejar como comentario dentro del código fuente
 el enunciado del problema."""


y=0
suma = 0

while y != -1 :
    suma = suma + y
    y=int(input("ingrese numero entero (finaliza con-1): "))
    
    
print("la suma total es: ",suma)

