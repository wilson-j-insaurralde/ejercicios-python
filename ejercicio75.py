# Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista.
# Imprimir la lista generada.

list= []
for f in range (5):
    valor = int(input("ingrese un valor entero:"))
    list.append(valor)

print (list)    