# Este es el Ejercicio 2.1 de Python

numero1 = int(input("Numero1:"))
numero2 = int(input("Numero2:"))

def mayorn(n1, n2):
    if n1 > n2:
        print("El numero mayor es:", n1, )
    elif n1 < n2:
        print("El numero mayor es:", n2, )

mayorn(numero1, numero2)