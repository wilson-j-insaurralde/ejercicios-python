"""Realizar la carga de enteros por teclado. Preguntar después que ingresa el valor si desea cargar
 otro valor debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
Mostrar la suma de los valores ingresados."""

opcion = "si"

suma = 0

while opcion == "si":

    valor = int(input("ingrese valor: "))

    suma = suma + valor 

    opcion=int(input("Desea cargar otro numero (si/no):"))

print("suma total: ", suma)

