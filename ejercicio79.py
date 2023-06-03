# Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados
# (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar los sueldos
# de los empleados agrupados en dos listas.
# Imprimir las dos listas de sueldos.

tarde = []
mañana = []

x = 0

for f in range (4):
    sueldo=float(input("ingrese sueldo de turno tarde :"))
    tarde.append(sueldo)
for f in range (4):
    sueldo2=float(input("ingrese sueldo de turno mañana :"))
    mañana.append(sueldo2)

print ("sueldos turno tarde: ", tarde)
print("sueldos turno mañana: ", mañana)