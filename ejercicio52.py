#Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
#Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante.
# Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

n = int(input("ingresar cantidad de puntos a procesar: "))
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0


for f in range (n):
    x = float(input("ingrese valor de X: "))
    y = float(input("ingrese valor de y: "))

    if x>0 and y >0:
        cont1 = cont1 + 1 
    else:    
        if x<0 and y>0:
            cont2=cont2 + 1
        else:
            if x<0 and y<0:
                cont3= cont3 + 1
            else:
              cont4= cont4 + 1
print("cantidad de puntos en el primer cuadrante: ",cont1)
print("cantidad de puntos en el segundo cuadrante: ",cont2)   
print("cantidad de puntos en el tercer cuadrante: ",cont3)   
print("cantidad de puntos en el cuarto cuadrante: ",cont4)    

