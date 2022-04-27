#ejercicio 1
#nombre=input("ingresa tu nombre: ")
#numero=int(input("ingresa un numero: "))
#print(nombre* numero)

#ejercicio 2
#numero1=(3+2)
#numero2=(2*5)
#numero3=(numero1/numero2)
#numero4=numero3**2
#numero4=pow(numero3,2)
#print(numero4)


#ejercicio 3
n=int(input("Ingrese un numero: "))
if n>=1:
    suma=(n*(n+1))/2
    suma=str(suma)
    n=str(n)
    print("la suma de los primeros numeros enteros positivos desde 1 hasta "+n+" es "+suma)
else:
    print("dije positivo")