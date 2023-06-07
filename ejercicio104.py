#Definir dos listas de 3 elementos.
#La primer lista cada elemento es una sublista con el nombre del padre y la madre de una familia.
#La segunda lista está constituida por listas con los nombres de los hijos de cada familia. Puede haber familias sin hijos.
#Imprimir los nombres del padre, la madre y sus hijos.
#También imprimir solo el nombre del padre y la cantidad de hijos que tiene dicho padre.

#Un ejemplo si se define por asignación:

#padres=[["juan","ana"], ["carlos","maria"], ["pedro","laura"]]
#hijos=[["marcos","alberto","silvia"], [], ["oscar"]]

padres = []
hijos= []

for p in range (3):
    pa=input("ingrese el nombre del padre: ")
    ma=input("ingrese el nombre de la madre: ")
    padres.append([pa,ma])
    
    x=int(input("ingrese cantidad de hijos de la pareja: "))
    hijos.append([])
    for j in range (x):
        hi=input("ingrese nombre del hijo: ")
        hijos[p].append(hi)

print("lista de padres, madres e hijos")
for k in range (3):
    print("padres: ",padres[k][0])
    print("madre:",padres[k][1])
    for x in range(len(hijos[k])):
        print("hijos: ",hijos[k][x])

print("Listado del padre y cantidad de hijos que tiene")
for x in range(3):
    print("padre:",padres[x][0])
    print("Cantidad de hijos:",len(hijos[x]))

