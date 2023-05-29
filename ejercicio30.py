# Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la 
# suma de los valores ingresados y su promedio.


y = 1
suma = 0
while y <= 10:
    
    num = int(input(" ingrese numero : "))
    suma = suma + num
    y = y + 1
    
promedio= suma/10
print("suma y promedio : ", suma , promedio)



