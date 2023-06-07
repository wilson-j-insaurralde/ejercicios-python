#Se desea saber la temperatura media trimestral de cuatro paises. Para ello se tiene como dato las temperaturas medias mensuales de dichos paises.
#Se debe ingresar el nombre del país y seguidamente las tres temperaturas medias mensuales.
#Seleccionar las estructuras de datos adecuadas para el almacenamiento de los datos en memoria.
#a - Cargar por teclado los nombres de los paises y las temperaturas medias mensuales.
#b - Imprimir los nombres de las paises y las temperaturas medias mensuales de las mismas.
#c - Calcular la temperatura media trimestral de cada país.
#c - Imprimir los nombres de los paises y las temperaturas medias trimestrales.
#b - Imprimir el nombre del pais con la temperatura media trimestral mayor.

paises = []
temperatura = []
media = []

for k in range (4):
    pa=input("ingrese pais: ")
    paises.append(pa)
    temperatura.append([])
    te1=float(input("ingrese temperatura 1: "))
    te2=float(input("ingrese temperatura 2: "))
    te3=float(input("ingrese temperatura 3: "))
    temperatura[k].append([te1,te2,te3])
    
    med=(te1+te2+te3)/3
    media.append(med)

for k in range(4):
    print("pais: ",paises)
    
    print("temp media mensual ", temperatura)

print("temperaturas medias trimestrales:")
for k in range(4):
    print("pais:",paises)
    print("temperatura media trimestral: ",media)

mayor=0
for k in range(1,4):
    if media[k]>media[mayor]:
        mayor=k

print("pais con la temperatura media trimestral mayor :")
print(paises[mayor],media[mayor])

            
