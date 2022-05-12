def sumar(num1, num2):
    num3=num1+num2
    print("el resultado de la suma entre "+str(num1)+" y "+str(num2)+" es: "+str(num3))

def restar(num1, num2):
    num3=num1-num2
    print("el resultado de la resta entre "+str(num1)+" y "+str(num2)+" es: "+str(num3))

def Multiplicar(num1, num2):
    num3=num1*num2
    print("el resultado de la multiplicacion entre "+str(num1)+" y "+str(num2)+" es: "+str(num3))

def Dividir(num1, num2):
    num3=num1/num2
    num3=round(num3,2)
    print("el resultado de la division entre "+str(num1)+" y "+str(num2)+" es: "+str(num3))
print("""bienvenido
que operacion desea realizar
1.- Sumar
2.- Restar
3.- Multiplicar
4.- Dividir
""")
opcion=int(input("Opcion: "))
num1=int(input("el primer numero: "))
num2=int(input("el segundo numero: "))

if opcion==1:
    sumar(num1, num2)
elif opcion==2:
    restar(num1, num2)
elif opcion==3:
    Multiplicar(num1, num2)
elif opcion==4:
    Dividir(num1, num2)