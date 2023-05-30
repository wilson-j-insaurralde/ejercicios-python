#Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base
# y la altura de un triángulo. El programa deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.

n = int(input("ingrese cantidad de numeros pares:"))

mayor = 0
cantidad = 0

for f in range (0,n,2):
    base = float(input("ingrese base: "))
    altura = float(input("ingrese altura: "))
    superficie = (base*altura)/2
    print("la superficie es de :",superficie)
    if superficie >= 12 :
        cantidad = cantidad + 1

print("la cantidad de triangulos mayores a 12: ",cantidad)
