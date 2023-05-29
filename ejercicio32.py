# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores
# o iguales a 7 y cuántos menores

x = 1
mayores = 0
menores = 0

while x <= 10 :
    nota = float(input("ingrese nota del alumno: "))
    if nota >= 7 :
        mayores = mayores + 1 

    else :
        menores = menores + 1

    x = x + 1 
print(mayores,"tienen nota mayoro igual a 7, ", menores, " tienen nota menores a 7")    