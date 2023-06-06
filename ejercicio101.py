# 21 - Listas: carga por teclado de componentes de tipo lista
#Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos notas,
# almacenar las notas en una lista paralela. Cada componente de la lista paralela debe ser también una lista
# con las dos notas. Imprimir luego cada nombre y sus dos notas.

#i cargáramos los datos por asignación sería algo parecido a esto:
#alumnos=["juan", "ana", "luis"]
#notas=[[10,8], [6,5], [2,8]]

nombres= []
notas = []

for x in range(3):
    nom=input("ingrese nombre del alumno: ")
    nombres.append(nom)
    not1=float(input("ingrese primer nota:"))
    not2=float(input("ingrese segunda nota:"))
    notas.append([not1,not2])

for x in range(3):
    print(nombres[x],notas[x])

