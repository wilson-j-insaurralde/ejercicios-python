# Definir por asignación una lista con 8 elementos enteros.
# Contar cuantos de dichos valores almacenan un valor superior a 100.

lista = [1,2,300,400,5,6,7,8]
cont = 0
x = 0
while x < len(lista):

    if lista[x] > 100 :
        cont = cont + 1
    x = x + 1     

print(cont)
