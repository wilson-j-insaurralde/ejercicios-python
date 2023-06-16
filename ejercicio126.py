# Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados:
#def retornar_superficie(lado1,lado2):
#En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cual de los dos tiene una superficie mayor.

def retornar_superficie(lado1,lado2):
    perimetro= lado1*lado2
    return perimetro

la1=float(input("ingrese primer lado: "))
la2=float(input("ingrese segundo lado: "))
print("la superficie es:", retornar_superficie(la1,la2))
perimetro1=retornar_superficie(la1,la2)
print("ingrese valores para el segundo rectangulo: ")
la1=float(input("ingrese primer lado: "))
la2=float(input("ingrese segundo lado: "))
print("la superficie es:", retornar_superficie(la1,la2))
perimetro2=retornar_superficie(la1,la2)

if perimetro1>perimetro2:
    print ("el primer rectangulo tiene mayor superficie de: ", perimetro1)
else: 
    print("el segundo rectangulo tiene mayor superficie de: ",perimetro2)

    