##Confeccionar un programa que pida por teclado tres notas de un alumno,
## calcule el promedio e imprima alguno de estos mensajes:
## Si el promedio es >=7 mostrar "Promocionado".
## Si el promedio es >=4 y <7 mostrar "Regular".
## Si el promedio es <4 mostrar "Reprobado".


not1=int(input("ingrese nota N°1: "))
not2=int(input("ingrese nota N°2: "))
not3=int(input("ingrese nota N°3: "))

suma = not1 + not2 + not3

promedio = suma/3

if promedio >= 7 :
    print("promocionado")
else :  
    if promedio >=4 and promedio <7:

      print("regular ")   
    else:
        print("reprobado")
