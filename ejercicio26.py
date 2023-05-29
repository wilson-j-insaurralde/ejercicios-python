#De un operario se conoce su sueldo y los años de antigüedad.
# Se pide confeccionar un programa que lea los datos de entrada e informe:
#a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %,
# mostrar el sueldo a pagar.
#b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
#c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.


operario = input ("nombre del o perario: ")
antiguedad = int(input("ingrese antiguedad:"))
sueldo = int(input("ingrese el sueldo del operario: "))


if sueldo < 500 and antiguedad >= 10:
    aumento = sueldo *1.20

    print (operario,"otorgar un aumento de:",(aumento-sueldo),"el sueldo a pagar es:", aumento  )
else:
    if sueldo < 500 and antiguedad < 10: 
       aumento = sueldo *1.05
       print (operario,"otorgar un aumento de:",(aumento-sueldo),"el sueldo a pagar es:", aumento  )
    else:
      print (operario,"el sueldo a pagar es:", sueldo )  

