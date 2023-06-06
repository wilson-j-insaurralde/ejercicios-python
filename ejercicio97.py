# Crear una lista por asignación. La lista tiene que tener 5 elementos. Cada elemento debe ser una lista,
# la primera lista tiene que tener un elemento, la segunda dos elementos,
# la tercera tres elementos y así sucesivamente.
# Sumar todos los valores de las listas.

list=[[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5]]
suma= 0
for x in range(len(list)):
    for j in range (len(list[x])):
        suma=suma+list[x][j]
print(suma)        
