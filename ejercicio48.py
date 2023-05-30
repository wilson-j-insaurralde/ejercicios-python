#Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos
# 5 valores ingresados.

cont = 0
cont2 = 0

for f in range(10):
    x = float(input("ingrese el numer: "))
    cont = cont + 1 
    if cont > 5:
        cont2=cont2 + x
print("la suma de los ultimos 5 valores es: ", cont2)
