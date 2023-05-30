# Escribir un programa que solicite por teclado 10 notas de alumnos y nos informe cuántos tienen notas
# mayores o iguales a 7 y cuántos menores.

mayor = 0
menor = 0

for x in range(10):
    y = float(input("ingrese nota: "))
    if y >=7 :
        mayor = mayor + 1
    else:
        menor = menor + 1   

print ("cantidad de notas mayores o iguales a 7: ", mayor)
print ("cantidad de notas menores a 7:", menor)