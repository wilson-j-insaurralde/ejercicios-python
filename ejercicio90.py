# Crear una lista y almacenar los nombres de 5 países. Ordenar alfabéticamente la lista e imprimirla

list=[]
aux=0

for j in range (5):
    pais=input("ingrese pais :")
    list.append(pais)
    
for x in range (4):
    for x in range (4):
        if list[x] > list[x+1]:
            aux = list[x+1]
            list[x+1]=list[x]
            list[x] = aux

print (list)