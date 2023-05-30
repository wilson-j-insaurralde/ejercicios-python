# Realizar un programa que lea los lados de n triángulos, e informar:
# a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales),
# isósceles (dos lados iguales), o escaleno (ningún lado igual)
# b) Cantidad de triángulos de cada tipo.

n = int(input("ingrese cantidad de triangulos: "))
cont1 = 0
cont2 = 0
cont3 = 0

for f in range(n):
    x = float(input("ingrese lado a: "))
    y = float(input("ingrese lado b: "))
    z = float(input("ingrese lado c: "))
if x==y and x==z:
    print( "el triangulo es equilatero")
    cont1 = cont1 + 1
else:
    if x==y or x==z or z==y :

      print("el triangulo es isoceles ")
      cont2 = cont2 + 1  
    else:
        print("el triangulo es escaleno ")
        cont3 = cont3 + 1   

print ("cantidad de triangulos equilateros: ",cont1)
print ("cantidad de triangulos isoceles: ",cont2)
print ("cantidad de triangulos escaleno: ",cont3)