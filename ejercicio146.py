#Confeccionar una función que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18 (como mínimo se envía un entero a la función)

def edades(v1,*lista):
    cont=0
    if v1>=18:
        cont=cont+1
    for j in range(len(lista)):
        if lista[j]>=18:
            cont=cont +1
    return cont 


mayores=edades(25,1,18,19,12,20,5)
print("mayores igual a 18:",mayores)