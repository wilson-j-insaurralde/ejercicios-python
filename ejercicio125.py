#Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado.


def perimetro(x):
    perimetro= x*x
    return perimetro
lado=float(input("ingrese el valor de un lado: "))
print("el perimetro es: ", perimetro(lado))