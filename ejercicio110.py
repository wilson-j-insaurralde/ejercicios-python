#Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
#Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
#Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)

empleados= []
sueldos = []
x=int(input("ingrese cantidad de empleados:"))

for j in range (x):
    em=input("ingrese nombre del empleado: ")
    empleados.append(em)
    sue=float(input("ingrese sueldo de dicho empleado: "))
    sueldos.append(sue)

posicion=0
while posicion<len(sueldos):
    if sueldos [posicion] > 10000:
        empleados.pop(posicion)
        sueldos.pop(posicion)
    else :
        posicion = posicion + 1
for k in range (posicion):
    print(empleados[k],sueldos[k])
    
