"""Realizar la carga de dos nombres de personas distintos. Mostrar por pantalla luego ordenados
 en forma alfabética."""

nombre1=input("Ingrese el primer nombre:")
nombre2=input("Ingrese el segundo nombre:")
print("Listado alfabetico:")
if nombre1<nombre2:
    print(nombre1)
    print(nombre2)
else:
    print(nombre2)
    print(nombre1)