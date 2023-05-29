# En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
# realizar un programa que lea los sueldos que cobra cada empleado e informe cuántos
# empleados cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá informar
# el importe que gasta la empresa en sueldos al personal.

n = int(input("ingrese numero de empleados : "))
x = 1
sumaSueldos = 0
mayores = 0
menores = 0

while x <= n:
    sueldo = float(input("ingrese el sueldo: "))
    sumaSueldos = sumaSueldos + sueldo

    if sueldo <= 300:
        menores = menores + 1
    else:
      mayores = mayores + 1 
    x = x + 1 

print(menores, " ganan entre 100 y 300")
print(mayores , " ganan mas de 300 ")
print("la empresa gasta en sueldos: ", sumaSueldos)
