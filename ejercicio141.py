#Confeccionar una función que reciba el nombre de un operario, el pago por hora y la cantidad de horas trabajadas. Debe mostrar su sueldo y el nombre. Hacer la llamada de la función mediante argumentos nombrados.

def operario(nombre,costohora,canthoras):
    costototal=costohora*canthoras
    print(nombre,"monto a pagar",costototal)


operario("juan",5,8)
