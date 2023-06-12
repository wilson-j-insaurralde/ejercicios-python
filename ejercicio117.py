# Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos. La carga de los valores hacerlo por teclado.

def mayor():
    x = float(input("ingrese valor :"))
    y= float(input("ingrese valor :"))
    z = float(input("ingrese valor :"))
    if x>y and x>z:
        print("el mayor es:",x)
    else:
        if y>x and y>z:
            print("el mayor es: ",y)
        else:
            print("el mayor es: ",z)

mayor()

            