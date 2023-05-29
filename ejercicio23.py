## Se ingresan por teclado tres números,
## si al menos uno de los valores ingresados es menor a 10,
## imprimir en pantalla la leyenda "Alguno de los números es menor a diez".

x=int(input("ingrese N°1: "))
y=int(input("ingrese N°2: "))
z=int(input("ingrese N°3: "))

if x < 10 or y < 10 or z < 10 : 
    print("al menos uno de los valores ingresados es menor a 10")
else:
    print ("ningun nomero ingresado es menor a 10")
