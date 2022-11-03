# Este es el Ejercicio 2.4 de Python

caracter = input("Proporciona un caracter:")                    #Escribir un caracter


def detectvocal(letra):                                         #Creacion de la funcion y asignar una variable
    vocales = ['a', 'e', 'i', 'o', 'u']                         #Creacion de una lista de vocales
    if letra in vocales:                                        #Condicional de si esta la letra(input) en la lista de vocales
        print("TRUE")                                           #Si esta en la lista muestra TRUE
    else:
        print("FALSE")                                          #Si no esta en la lista muestra FALSE

detectvocal(caracter)                                           #Llamada de la funcion (caracter=letra)