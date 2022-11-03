# Este es el Ejercicio 2.2 de Python

numero1 = int(input("Numero1:"))
numero2 = int(input("Numero2:"))
numero3 = int(input("Numero3:"))


def mayorn(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print("El numero mayor es:", n1, )
    elif n2 > n1 and n2 > n3:
        print("El numero mayor es:", n2, )
    elif n3 > n1 and n3 > n2:
        print("El numero mayor es:", n3, )

mayorn(numero1, numero2, numero3)
