#Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
#En el bloque principal iniciamos por asignación la lista de string:
#palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
#print("Palabra con mas caracteres:",mascaracteres(palabras))

def masCaracteres(palabras):
    cont=palabras[0]
    for j in range(1,len(palabras)):
        if len(palabras[j])>len(cont):
            cont=palabras[j]

    return cont
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]

print ("palabra con mas caracteres: ", masCaracteres(palabras))

