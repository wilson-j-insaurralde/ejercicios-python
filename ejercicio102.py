#Se tiene que cargar la siguiente información:
#· Nombres de 3 empleados
#· Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses.
#Confeccionar el programa para:

#a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado.
#b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado.
#c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses
#d) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado


empleados=[]
sueldo=[]
acumulado=[]

for x in range(3):
    emp=input("ingrese el nombre del empleado : ")
    suel1=float(input("ingrese primer sueldo del empleado: "))
    suel2=float(input("ingrese segundo sueldo del empleado: "))
    suel3=float(input("ingrese tercer sueldo del empleado: "))
    empleados.append(emp)
    sueldo.append([suel1,suel2,suel3])
    suma= suel1 + suel2 + suel3
    acumulado.append(suma)
for x in range(3):
    print(empleados[x], sueldo[x])

print("sueldo acumulados:")
for x in range(3):
    print(empleados[x], acumulado[x])

posmayor= 0
mayor = acumulado[0]
for x in range(1,3):
    if acumulado[x]>mayor:
        mayor= acumulado[x]
        posmayor=x

print("Empleado con mayores ingresos en los ultimos tres meses")
print(empleados[posmayor])
print("con un ingreso de",mayor)
