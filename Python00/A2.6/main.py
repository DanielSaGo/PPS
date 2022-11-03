# Este es el Ejercicio 2.6 de Python

cadena = ("Mi nombre es Daniel")

def inversa(palabra):
    cadenainv = ""
    for i in palabra:
        cadenainv = i+ cadenainv
    print(cadenainv)

inversa(cadena)
