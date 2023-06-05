#Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo.
#Ordenar alfabéticamente e imprimir los resultados. Por último ordenar con respecto a la cantidad de habitantes
#(de mayor a menor) e imprimir nuevamente.
paises= []
habitantes= []
aux1=0
aux2=0
for j in range(5):
    pa=input("ingrese pais: ")
    hab=int(input("ingrese cantidad de habitantes: "))
    paises.append(pa)
    habitantes.append(hab)

for k  in range (4):
    for x in range(4):
        if paises[x]>paises[x+1]:
            aux1=paises[x+1]
            paises[x+1]=paises[x]
            paises[x]=aux1
            aux2=habitantes[x+1]
            habitantes[x+1]=habitantes[x]
            habitantes[x]=aux2
print("orden alfabetico:")
for ñ in range(5):
    print(paises[ñ],habitantes[ñ])    


for k  in range (4):
    for x in range(4):
        if habitantes[x]<habitantes[x+1]:
            aux1=paises[x+1]
            paises[x+1]=paises[x]
            paises[x]=aux1
            aux2=habitantes[x+1]
            habitantes[x+1]=habitantes[x]
            habitantes[x]=aux2
print("orden por cantidad de habitantes: ")
for ñ in range(5):
    print(paises[ñ],habitantes[ñ])      
