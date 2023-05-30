# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.

cont1 = 0 
cont2 = 0
mult15 = 0
pares = 0

for f in range (10):
    x = float(int("ingrese numero: "))
    if x<0 :
        cont1 = cont1 + 1 
    else:   
        if x>0:
            cont2 = cont2 + 1
    if x%15 == 0 :
        mult15 = mult15 + 1
    if x%2 == 0:
        pares = pares +1 

print("cantidad de valores positivos: ", cont2)
print("cantidad de valores negativos: ",cont1)
print("cantidad multiplos de 15: ", mult15)
print("cantidad de numeros pares: ",pares)
