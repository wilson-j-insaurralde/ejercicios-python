#Se ingresan tres valores por teclado,
# si todos son iguales se imprime la suma del primero con el segundo y
# a este resultado se lo multiplica por el tercero.


x=int(input("ingrese N°1: "))
y=int(input("ingrese N°2: "))
z=int(input("ingrese N°3: "))

if x == y and x == z :
    operacion = (x + y)* z 
    print("operacion=" ,operacion )
else:
    print ("los numeros no son iguales ") 




