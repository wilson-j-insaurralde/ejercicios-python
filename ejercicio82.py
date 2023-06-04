# Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista.
#  Mostrar el nombre de persona menor en orden alfabético

nombres = []

for j in range (5):
    name = input("ingrese nombre: ")
    nombres.append(name)

x = nombres[0]

for j in range (1,5):
    if nombres[j]< x:
        x = nombres[j]

print (nombres)

print ("menor: ", x)
