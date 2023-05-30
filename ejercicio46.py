#Codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o iguales a 1000 
# (n se carga por teclado)
# Este tipo de problemas también se puede resolver empleando la estructura repetitiva for.
# Lo primero que se hace es cargar una variable que indique la cantidad de valores a ingresar.
# Dicha variable se carga antes de entrar a la estructura repetitiva for.

n = int(input("ingrese cantidad de numeros: "))
mayores = 0
menores = 0
for f in range (n):
    x = float(input("ingrese numeros :"))
    if x >= 1000 :
        mayores = mayores + 1 

    else:
        menores = menores + 1 
print("cantidad de numeros mayores o igual a 1000: ", mayores)
print ("cantidad de numeros menores a 1000: ", menores)
