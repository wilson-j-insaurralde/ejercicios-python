#ejemplo

"""nombre='juan'
print(nombre[0])   #se imprime una j
if nombre[0]=="j": #verificamos si el primer caracter del string es una j
    print(nombre)
    print("comienza con la letra j")"""

"""Realizar la carga del nombre de una persona y luego mostrar el primer caracter del nombre y
 la cantidad de letras que lo componen."""

nombre = input("ingrese nombre: ")
print("primer caracter del nombre: ",nombre[0])

print("cantidad de letras del nombre: ",len(nombre))
