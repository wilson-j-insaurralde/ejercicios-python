#Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en una tupla)
#El programa debe tener las siguientes funciones:
#1)Carga de los nombres de empleados y sus últimos tres sueldos.
#2)Imprimir el monto total cobrado por cada empleado.
#3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses.
#Tener en cuenta que la estructura de datos si se carga por asignación debería ser similar a:
#empleados = [["juan",(2000,3000,4233)] , ["ana",(3444,1000,5333)] ,  etc.   ]

def empleados():
    lista=[]
    
    for j in range (5):
        name=input("ingrese nombre: ")
        val1=float(input("ingrese primer sueldo: "))
        val2=float(input("ingrese segundo sueldo: "))
        val3=float(input("ingrese tercer sueldo: "))
        
        lista.append([name,(val1,val2,val3)])
    return lista


def ganancias(lista):
    print("monto total ganado por el empleado en los ultimos 3 meses: ")
    for j in range(5):
        total=lista[j][1][0]+lista[j][1][1]+lista[j][1][2]
        print(lista[j][0],total)

def mayor(lista):
    print("empleados que tuvieron un ingreso trimestral mayor a 1000: ")
    for j in range (5):
        total=lista[j][1][0]+lista[j][1][1]+lista[j][1][2]
        if total>1000:
            print(lista[j][0])
    return


lista=empleados()
ganancias(lista)
mayor(lista)



        

        