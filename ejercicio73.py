# Definir una lista por asignación con 5 enteros.
# Mostrar por pantalla solo los elementos con valor iguales o superiores a 7


list = [1,7,8,9,3]
cont = 0
x = 0
while x < len(list):
    if list[x] > 7:
        print (list[x])
    x = x + 1 
    