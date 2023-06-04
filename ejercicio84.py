# Desarrollar un programa que permita cargar 5 nombres de personas y sus edades respectivas.
# Luego de realizar la carga por teclado de todos los datos imprimir los nombres de las personas
# mayores de edad (mayores o iguales a 18 años)

nombres = []
edades = []
mayores = []
x = 0

for j in range (5):
    name= input("ingrese nombre: ")
    age = int(input("ingrese edad :"))
    nombres.append(name)
    edades.append(age)
    
for j in range (5):
   if edades[j] >= 18:
       mayores.append(nombres[j])

print ("los mayores son: ",mayores)
