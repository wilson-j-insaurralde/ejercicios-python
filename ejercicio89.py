# Se debe crear y cargar una lista donde almacenar 5 sueldos. Ordenar de menor a mayor la lista.

sueldos = []
aux=0

print("carga de suledos:")
for j in range (5):
    sul=float(input("ingrese sueldo:"))
    sueldos.append(sul)

j=0

for x in range(4):   
    for j in range (4):
        if sueldos[j] > sueldos[j+1]:
            aux= sueldos[j]
            sueldos [j]= sueldos[j+1]
            sueldos[j+1]=aux
print("lista ordenada: ", sueldos)