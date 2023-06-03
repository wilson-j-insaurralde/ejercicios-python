# Realizar la carga de valores enteros por teclado, almacenarlos en una lista.
# Finalizar la carga de enteros al ingresar el cero. Mostrar finalmente el tamaño de la lista.

list = []

while (True):
    valor = int(input("ingrese valores enteros: "))
    if valor == 0 : break
    list.append(valor)
print(len(list))
    





