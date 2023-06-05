# Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas.
# Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los alumnos.

nombres= []
notas= []
aux1=0
aux2=0

for j in range(5):
    name=input("ingrese nombre: ")
    note=float(input("ingrese nota: "))
    nombres.append(name)
    notas.append(note)

for k in range(4):
    for x in range (4):
        if notas[x]<notas[x+1]:
            aux1=notas[x+1]
            notas[x+1]=notas[x]
            notas[x]= aux1

            aux2=nombres[x+1]
            nombres[x+1]=nombres[x]
            nombres[x]= aux2

for x in range (5):
    print ("alumnos:", nombres[x] ,notas[x] )


