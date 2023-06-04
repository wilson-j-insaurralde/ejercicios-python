# En un curso de 4 alumnos se registraron las notas de sus exámenes y se deben procesar de acuerdo a 
#lo siguiente:
#a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas paralelas)
#b) Realizar un listado que muestre los nombres, notas y condición del alumno. En la condición,
# colocar "Muy Bueno" si la nota es mayor o igual a 8, "Bueno" si la nota está entre 4 y 7, y colocar
# "Insuficiente" si la nota es inferior a 4.
#c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”.


nombres=[]
notas=[]
for x in range(4):
    nom=input("Ingrese nombre del alumno:")
    nombres.append(nom)
    no=int(input("Ingrese la nota de dicho alumno:"))
    notas.append(no)

cantidad=0
for x in range(4):
    print(nombres[x])
    print(notas[x])
    if notas[x]>=8:
        print("Muy Bueno")
        cantidad=cantidad+1
    else:
        if notas[x]>=4:
            print("Bueno")
        else:
            print("Insuficiente")

print("La cantidad de alumnos muy buenos son")
print(cantidad)
