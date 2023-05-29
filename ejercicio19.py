## Confeccionar un programa que lea por teclado tres números enteros distintos y nos muestre el mayor.
x = int(input("ingrese primer numero "))
y = int(input("ingrese segundo numero "))
z = int(input("ingrese tercer numero "))

if x > y and x > z:
    print("el mayor es: ",x)
else:
    if y > z :
        print("el mayor es: ",y)  
    else:
        print("el mayor es: ",z)    


        
