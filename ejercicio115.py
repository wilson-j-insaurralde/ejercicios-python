#Desarrollar un programa que solicite la carga de tres valores y muestre el menor. Desde el bloque principal del programa llamar 2 veces a dicha función (sin utilizar una estructura repetitiva)

def menor3():
    x=float(input("ingrese primer valor: "))
    y=float(input("ingrese segundo valor: "))
    z=float(input("ingrese tercer valor: "))
    if x<y and x<z :
        print("el menor es: ",x)
    else: 
        if y<x and y<z:
            print("el menor es: ",y)
        else:
            print("el menor es: ",z )


menor3()
menor3()