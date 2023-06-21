#confeccionar una funcion que tenga 3 enteros y retorne la suma. llamar a la funcion enviando 3 enteros que se encuentran almacenados en una lista.

def sumar(v1, v2, v3):
    return v1 + v2 + v3

li=[2, 4, 5]
su=sumar(*li)
print(su)