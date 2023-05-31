"""Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron.
 Tener en cuenta que un espacio en blanco es igual a
" ", en cambio una cadena vacía es """""

oracion = input("ingrese oracion: ")

x = 0
cont = 0

while x < len(oracion):
    if oracion[x] == " ":
        cont = cont + 1 
        
    x = x + 1

print("la oracion pose",cont,"espacios en blanco")
