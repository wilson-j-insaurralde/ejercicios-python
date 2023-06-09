#Desarrollar un programa con dos funciones. La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor. La segunda que solicite la carga de dos valores y muestre el producto de los mismos. LLamar desde el bloque del programa principal a ambas funciones.

def cuadrado():
    x=int(input("ingrese el valor: "))
    cuadrado= x**2
    print("el cuadrado es: ", cuadrado)

def producto():
    x=float(input("ingrese primer numero: "))
    y=float(input("ingrese segundo numero: "))
    pro=x*y
    print("producto de los numeros: ",pro)

cuadrado()
producto()
