#Escribir un programa que pida ingresar la coordenada de un punto en el plano,
# es decir dos valores enteros x e y (distintos a cero).
# Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto.
# (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)

x = int(input("ingrese los valores de x: " ))
y = int(input("ingrese valores de y : "))

if x > 0 and y > 0 :
    print("se encuentra en el primer cuadrante ")
else:
    if x < 0 and y > 0 :
        print("se encuentra en el segundo  cuadrante ")   
    else:
        if y < 0 and x > 0 :
           print("se encuentra en el cuarto cuadrante ")  

        else:

            print("se encuentra en el tercer  cuadrante ")  
