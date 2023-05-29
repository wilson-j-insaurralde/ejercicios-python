# Una planta que fabrica perfiles de hierro posee un lote de n piezas.
# Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y 
# luego ingrese la longitud de cada perfil; sabiendo que la pieza cuya longitud esté comprendida
# en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.

n = int(input("ingrese cantidad de piezas:"))
x = 1
z = 0
j = 0
while x <= n:
    y = float(input("ingrese longitud de la pieza metros: "))
    if y >= 1.20 and y <= 1.30 :
        z = z + 1
    else:
        j = j + 1 



    x = x + 1 
print("la cantidad de piezas utiles son: ", z)
print ("la cantidad de piezas no aptas son: ", j)
