# Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.
# Repetir la carga e impresion de la suma 5 veces.
# Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.


def carga_suma():
    x=int(input("ingrese valor entero"))
    y=int(input("ingrese valor entero"))
    suma = x+y
    print("suma: ",suma)
def separacion():
    print("-------------------------------------------------------")    

for x in range (5):
    carga_suma()
    separacion()

