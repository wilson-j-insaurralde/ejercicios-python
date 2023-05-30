#Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente 
#la suma de los valores ingresados y su promedio. Este problema ya lo desarrollamos, lo resolveremos 
#empleando la estructura for para repetir la carga de los diez valores por teclado.


suma = 0

for x in range(1,11):
    y = float(input("ingrese valor: "))
    suma = suma + y

promedio = suma/10
print("suma de valores ingresados: ",suma)
print("promedio de valores ingresados: ",promedio)
