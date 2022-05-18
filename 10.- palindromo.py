#palindromo

# Escribir un programa que identifique 
# si una palabra es palindromo o no
# ejemplo: luz azul
# ana
# anita lava al tina
# yo hago yoga hoy


def palindromo(palabra):
    palabra=palabra.replace(' ','')
    palabra=palabra.lower()
    if palabra==palabra[::-1]:
        return True
    else:
        return False

#funcion principal main/run
def main():
    palabra=input("ingrese una frase o palabra por favor: ")
    es_palindromo=palindromo(palabra)
    if es_palindromo:
        print("es palíndromo")
    else:
        print("no es palíndromo")
# punto de entrada
# buena practica

if __name__=="__main__":
    main()

