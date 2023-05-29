## Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras
## y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. 
## Mostrar un mensaje de error si el número de cifras es mayor.

x = int(input("ingrese numero: "))

if x > 0 :
    if x < 10:
     print ("el numero es de una cifra ")
    else:
       if x < 100 :
          print("el numero es de dos cifras")
       else:
          if x < 1000:
            print("el numero es de 3 cifras")
          else:
             print("el numero es mayor a tres cifras")

else:   
   print("el numero no es valido")  
   


