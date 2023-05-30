#Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados
# fueron múltiplos de 3 y cuántos de 5. Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 
# a la vez.

mult3 = 0
mult5 = 0

for f in range (10):
    x = int(input("ingrese numero: "))
    if x%3 == 0:
        mult3 = mult3 + 1 
    if x%5 == 0:
        mult5 = mult5 + 1 

print("Cantidad de valores ingresados múltiplos de 3")
print(mult3)
print("Cantidad de valores ingresados múltiplos de 5")
print(mult5)