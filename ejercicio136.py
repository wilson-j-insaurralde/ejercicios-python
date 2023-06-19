#En una empresa se almacenaron los sueldos de 10 personas.
#Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
#1) Carga de los sueldos en una lista.
#2) Impresión de todos los sueldos.
#3) Cuántos tienen un sueldo superior a $4000.
#4) Retornar el promedio de los sueldos.
#5) Mostrar todos los sueldos que están por debajo del promedio.

def sueldos():
    nombre=[]
    sueldo=[]
    for j in range (10):
        nom=input("ingrese nombre del emplado: ")
        suel=float(input("ingrese el sueldo de dicho empleado: "))
        nombre.append(nom)
        sueldo.append(suel)
    print(nombre)
    print(sueldo)
    return (nombre,sueldo)

def superior(sueldo):
    cont=0
    for j in range(10):
        if sueldo[j]>4000:
            cont=cont+1
    print (cont,"poseen sueldos mayores a 4000")
    return cont
def promedio(sueldo):
    suma=0
    for j in range(10):
        suma = suma + sueldo[j]


    promedio2 =suma/10   
    print("el promedio de los sueldos es: ",promedio2)
    
    return promedio2
def menores(nombre,sueldo,promedio):
    print("poseen sueldo menores al promedio")
    for j in range (10):
        if sueldo[j]<promedio:
            
            print(nombre[j],sueldo[j])
            


nombre,sueldo=sueldos()
superior(sueldo)
promedio2=promedio(sueldo)
menores(nombre,sueldo,promedio2)