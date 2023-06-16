# Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

def promedio(x,y,z):
    suma= x+y+z
    pro=suma/3
    return pro
    
va1=int(input("ingrese primer valor entero: "))
va2=int(input("ingrese segundo valor entero: "))
va3=int(input("ingrece tercer valor entero: "))

print("el promedio es:",promedio(va1,va2,va3))
