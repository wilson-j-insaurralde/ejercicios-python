#Confeccionar un programa con las siguientes funciones:
#1)Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
#2)Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados y muestre el nombre del empleado con sueldo mayor.
#En el bloque principal del programa llamar dos veces a la función de carga y seguidamente llamar a la función que muestra el nombre de empleado con sueldo mayor.
# bloque principal

#empleado1=cargar_empleado()
#empleado2=cargar_empleado()
#mayor_sueldo(empleado1,empleado2)


def carga():
    name=[]
    sueldo=[]
    while (True):
        print("ingrese fin para finalizar carga.")
        na=input("ingrese el nombre: ")       
        if na == "fin" :break
        name.append(na) 
        sue=float(input("ingrese el sueldo de dicho empleado: "))
        sueldo.append(sue)  
    print(name)
    print(sueldo)    
    return (name,sueldo)

def suledoMayor(name,sueldo):
    mayor=sueldo[0]
    for j in range(1,len(sueldo)):
        if sueldo[j]>mayor:
            mayor=sueldo[j]
            nombre=name[j]
    return(mayor,nombre) 

nombre,sueldo=carga()
mayor,name=suledoMayor(nombre,sueldo)  
print("la persona con mayor sueldo es:",name )
print("ganando: ",mayor)  
