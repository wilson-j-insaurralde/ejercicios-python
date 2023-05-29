##Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.
x=int(input("ingrese N°1: "))
y=int(input("ingrese N°2: "))
z=int(input("ingrese N°3: "))

cont = 0
if x > y :
    if x > z:
        print("el mayor es :" , x)
    else :
        print("el mayor es :" , z)
else:
    if y > z :
        print("el mayor es :" , y)
    else:
        print("el mayor es :" , z)