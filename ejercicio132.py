#Definir una lista de enteros por asignación en el bloque principal. Llamar a una función que reciba la lista y nos retorne el producto de todos sus elementos. Mostrar dicho producto en el bloque principal de nuestro programa.



total = 0 
lista = [] 
while (True):
    inp= input("ingrese numero entero(para finalizar ingresar(fin))): ")
    if inp == "fin" : break
    ap=int(inp)
    lista.append(ap) 


print ("la lista es: ",lista)


def producto(x):
    cont=x[0]   
    for j in range (1,len(x)):
        cont=cont * x[j]
    return cont
print("el producto de todos sus elementos es: ", producto(lista))
