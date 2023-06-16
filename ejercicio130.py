#Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y un segundo parámetro de tipo entero. Dentro de la función mostrar cada elemento de la lista multiplicado por el valor entero enviado.

#lista=[3, 7, 8, 10, 2]
#multiplicar(lista,3)


def multiplicar(x,y):
    lista=[]
    for j in range(len(x)):
        val=x[j]*y
        lista.append(val)
    return lista

x=[3, 7, 8, 10, 2]
y = 3 
print(multiplicar(x,y))

