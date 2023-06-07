"""Definir una lista y almacenar los nombres de 3 empleados.
Por otro lado definir otra lista y almacenar en cada elemento una sublista con los números de días del mes que el empleado faltó.
Imprimir los nombres de empleados y los días que faltó.
Mostrar los empleados con la cantidad de inasistencias.
Finalmente mostrar el nombre o los nombres de empleados que faltaron menos días."""


empleado=[]
faltas=[]
for k in range (3):
    em= input("ingrese nombre del empleado: ")
    empleado.append(em)
    cant=int(input("ingrese cantidad de dias que falto: "))
    faltas.append([])
    for x in range (cant):
        dia=int(input("ingrese el numero del dia que falto: "))
        faltas[k].append(dia)

for k in range(3):
    print("empleado: ",empleado[k])
    for x in range (len(faltas[k])):
        print("falto los dias:", faltas[k][x])


print("Nombres de empleados y cantidad de inasistencias")
for x in range(3):
    print(empleado[x],len(faltas[x]))


men=len(faltas[0])
for x in range(1,3):
    if len(faltas[x])<men:
        men=len(faltas[x])

print("Empleado o empleados que faltaron menos")
for x in range(3):
    if len(faltas[x])==men:
           print(empleado[x])


           