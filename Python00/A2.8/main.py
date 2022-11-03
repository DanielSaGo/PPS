# Este es el Ejercicio 2.8 de Pytho

n = int(input("Proporcione un numero:"))
c = str(input("Proporcione un caracter:"))

def funmulti(numero, caracter):
    multi = numero*caracter
    print("Caracter multiplicado por el numero:", multi)

funmulti(n, c)