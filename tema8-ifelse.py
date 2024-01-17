num1=int(input("Ingresa el primer numero:D "))
num2=int(input("Ingresa el segundo numero:D "))

if num1>num2:
    print("El {} es mayor que el {}".format(num1,num2))
else:
    print("El {} es mayor que el {}".format(num1,num2))
    
print("_________________Dame una edad________________________")
edad=int(input("Ingresa tu edad"))

if edad>18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 18")
else:
    print("Eres menor de edad")