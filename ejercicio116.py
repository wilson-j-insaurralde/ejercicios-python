#Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.



def mostrar_mensaje(mensaje):
    print("*************************************************")
    print(mensaje)
    print("*************************************************")

def programa():
    x=float(input("ingrese valor: "))
    y=float(input("ingrese otro valor "))
    suma=x+y
    print("la suma es: ",suma)
    
mostrar_mensaje("El programa calcula la suma de dos valores ingresados por teclado.")
programa()
mostrar_mensaje("Gracias por utilizar este programa")

