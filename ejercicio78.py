# Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float)
# Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.


list = []
x = 0 
suma = 0
cont1 = 0
cont2 = 0
for f in range(5):
    valor = float(input("ingrese altura: "))
    list.append(valor)
    suma = suma + valor 

promedio = suma / 5 

while x < len(list):
    if  list[x] > promedio :
        cont1 = cont1 + 1 
    else:
        cont2 = cont2 +1 
    x = x + 1    
print ("promedio: ", promedio)

print("personas mas altas que el promedio: ",cont1 )

print ("personas mas bajas que el promedio: ",cont2 )