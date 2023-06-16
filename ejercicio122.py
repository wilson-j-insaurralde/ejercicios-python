#Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.

def mayor (x,y):
    if x > y :
        print (x," es el mayor")
    else: 
        print(y," es el mayor ")

valor1=float(input("ingrese primer valor: "))
valor2=float(input("ingrese el segundo valor: "))
print(mayor(valor1,valor2))