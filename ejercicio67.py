"""Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas.
 Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas para que sea
   más fácil disponer la condición que verifica que es una vocal."""

y = input("ingrece oracion: ")
oracion = y.lower()
x = 0
cont = 0 

while x < len(oracion):
    
    if oracion[x]=="a" or oracion[x]=="e" or oracion[x]=="i" or oracion[x]=="o" or oracion[x]=="u":
        cont = cont + 1
    x = x + 1 
print("la oracion posee ",cont," bocales.")

