##Se ingresan tres notas de un alumno,
## si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado"

not1=int(input("ingrese nota N°1: "))
not2=int(input("ingrese nota N°2: "))
not3=int(input("ingrese nota N°3: "))

suma = not1 + not2 + not3
promedio = suma/3
if promedio > 7 :
    print("promocionado")
else : 
    print("no promociona ")   
