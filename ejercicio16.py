## Se ingresa por teclado un valor entero,
## mostrar una leyenda que indique si el número es positivo,
## negativo o nulo (es decir cero)


x = int(input("ingrese numero: "))

if x == 0 :
   print("el valor es nulo ")
else:
   if x > 0 :
       print("el valor es positivo")
   else:
       print("el valor es negativo")

       