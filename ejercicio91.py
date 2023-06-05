# Solicitar por teclado la cantidad de empleados que tiene la empresa.
# Crear y cargar una lista con todos los sueldos de dichos empleados.
# Imprimir la lista de sueldos ordenamos de menor a mayor.


x = int(input("ingrese cantidad de emplados de la empresa: "))
sueldos = []
aux = 0 
print("carga de sueldos ")
for j in range (x):
    su= float(input("ingrese suledo:"))
    sueldos.append(su)

for j in range (x-1): 
    for z in range (x-1):
        if sueldos[z] > sueldos[z+1]:
            aux= sueldos[z+1]
            sueldos[z+1]=sueldos[z]
            sueldos[z]=aux 

print("lista de sueldos ordenados de menor a mayor: ", sueldos)
