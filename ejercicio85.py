# Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra.
# Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado.

producto = []
precio = []

for j in range(5):
    pro=input("ingrese producto: ")
    pre=float(input("ingrese precio del producto: "))
    producto.append(pro)
    precio.append(pre)

x = precio[0]
promayor = []
premayor = []


for j in range(5):
    if precio[j] > x :
        promayor.append(producto[j])
        premayor.append(precio[j])

print ("productos mayores: ", promayor)
print ("precios: ", premayor)