#Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas. Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas mayores de edad (mayores o iguales a 18 años)
#Imprimir la edad promedio de las personas.

def nombresEdades():
    nombre=[]
    edad=[]
    
    for j in range (5):
        nom=input("ingrese nombre de la persona: ")
        ed=int(input("ingrese la edad de dicha persona: "))
        nombre.append(nom)
        edad.append(ed)
    return [nombre,edad]

def mayores(nombre,edad):
    print("mayores de edad: ")
    for j in range (5):
        if edad[j]>=18:
            print (nombre[j],edad[j])

def promedioEdad(edad):
    suma=0
    for j in range (5):
        suma= edad[j]+suma
    promedio= suma/5
    print("el promedio de edad es: ",promedio)
    return promedio
nombres,edades=nombresEdades()
mayores(nombres,edades)
promedioEdad(edades)

