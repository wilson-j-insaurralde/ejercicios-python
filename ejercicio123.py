# Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene. En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.

def longitud(x):
    return len(x)

nombre1=input("ingrese nombre: ")
nombre2=input("ingrese otro nombre: ")
long1=longitud(nombre1)
long2=longitud(nombre2)
if long1==long2:
    print("los nombre tienen la misma cantidad de letras: ",nombre1,nombre2)
else:
    if long1>long2:
        print(nombre1,"tiene mayor cantidad de letras.") 
    else:
        print(nombre2,"tiene mayor cantidad de letras.") 
