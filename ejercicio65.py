"""Métodos propios de las cadenas de caracteres.
Los string tienen una serie de métodos (funciones aplicables solo a los string) que nos facilitan la
 creación de nuestros programas.

Los primeros tres métodos que veremos se llaman: lower, upper y capitalize.

upper() : devuelve una cadena de caracteres convertida todos sus caracteres a mayúsculas.
lower() : devuelve una cadena de caracteres convertida todos sus caracteres a minúsculas.
capitalize() : devuelve una cadena de caracteres convertida a mayúscula solo su primer caracter
 y todos los demás a minúsculas."""

"""Inicializar un string con la cadena "mAriA" luego llamar a sus métodos upper(),
 lower() y capitalize(), guardar los datos retornados en otros string y mostrarlos por pantalla."""
 
nombre1="mAriA"
print(nombre1)
nombre2=nombre1.upper()
print(nombre2)
nombre3=nombre1.lower()
print(nombre3)
nombre4=nombre1.capitalize()
print(nombre4)