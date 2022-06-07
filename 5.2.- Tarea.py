# Tarea 1
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y 
# muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

payaso=112
muñeca=75

numeropaya=int(input("cantidad de payasos vendidos: "))
numeromuñe=int(input("cantidad de muñecas vendidas: "))

totalpaya=numeropaya*payaso
totalmuñe=numeromuñe*muñeca
total=totalpaya+totalmuñe
total=str(total)
totalpaya=str(totalpaya)
totalmuñe=str(totalmuñe)

print("Peso total del paquete de payasos: "+totalpaya)
print("Peso total del paquete de muñecas: "+totalmuñe)

print("El peso total del paquete es: "+total)


# Tarea 2
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase 
# "Tu índice de masa corporal es <imc>" donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso=int(input("Digite su peso en KG: "))
estatura=float(input("Digite su estatura en metros: "))

if estatura<2.51:
    if estatura>0.63:
        if peso<594:
            if peso>25:
                IMC=peso/pow(estatura, 2)
                IMC=round(IMC,2)
                IMC=str(IMC)
                print("Tu índice de masa corporal es "+IMC)
            else:
                print("peso no valido")
        else:
            print("peso no valido")
    else:
        print("estatura no valida")
else:
    print("estatura no valida")
