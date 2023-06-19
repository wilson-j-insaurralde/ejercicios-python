#Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
#Definir las siguientes funciones:
#1) Cargar los nombres de articulos y sus precios.
#2) Imprimir los nombres y precios.
#3) Imprimir el nombre de artículo con un precio mayor
#4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.


def articulo():
    nombre=[]
    precio=[]
    for j in range (5):
        nom=input("ingrese nombre del producto: ")
        suel=float(input("ingrese precio de dicho producto: "))
        nombre.append(nom)
        precio.append(suel)
    print(nombre)
    print(precio)
    return (nombre,precio)

def mayores(nombre,precio):
    mayor=precio[0]
    
    for j in range (1,5):
        if precio[j]>mayor:
            mayor=precio[j]
            name=nombre[j]
    print("el producto de mayor precio es: ")
    print(name,mayor)
    return mayor   
def importeMayores(importe,nombre,precio):
    print ("productos con mayor valor del ingresado:")
    for j in range (5):
        if precio[j]>=importe:
            
            print(nombre[j],precio[j])

nombre,precio=articulo()     
mayores(nombre,precio)
importe=float(input("ingrese importe: "))
importeMayores(importe,nombre,precio)      