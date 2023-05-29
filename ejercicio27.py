#Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e
# informe su rango de variación (debe mostrar el mayor y el menor de ellos)


x=int(input("ingrese N°1: "))
y=int(input("ingrese N°2: "))
z=int(input("ingrese N°3: "))

if x < y and x < z :
    print("el menor es: ", x)
else:
    if y < z:
       print ("el menor es " ,y)
    else:
        print("el menor es: ", z)
if x > y and x > z :
    print("el mayor es:" , x)
else: 
    if y > z :
        print ("el mayor es: ",y)
    else:

        print("el mayor es: ", z)

