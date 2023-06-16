# Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.

def superficie(x):
    
    superficie= x*x
    return superficie

va=int(input("Ingrese el valor del lado del cuafrado:"))
superficie=superficie(va)
print("La superficie del cuadrado es",superficie)
