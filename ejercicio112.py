#Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.
#Implementar estas actividades en tres funciones.

def presentacion ():
     print("Programa que permite cargar dos valores por teclado.")
     print("Efectua la suma de los valores")
     print("Muestra el resultado de la suma")
     print("*******************************")

def sumadevalores ():
     valor1=float(input("ingrese primer valor: "))
     valor2=float(input("ingrese segundo valor: "))
     suma=valor1+valor2
     print("la suma es:", suma)

def finalizacion():
    print("*******************************")    
    print("Gracias por utilizar este programa")

presentacion()
sumadevalores()
finalizacion()