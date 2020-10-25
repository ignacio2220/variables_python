#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.4

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Ignacio Melchiori"
__email__ = "melchiorignacio@gmail.com"
__version__ = "1.4"

def ej1():
    # Ejercicios de práctica numérica
    numero_1 = 5
    numero_2 = 7

    suma = numero_1 + numero_2 # Realizar la suma de las dos variables
    # numero_1 y numero_2
    # Almacenar el valor de la suma en una variable
    # ej:
    # operacion = .....

    # Imprimir en pantalla el resultado de la suma
    # print(....)
    print('El resultado de la suma es', suma)
    # Repita el procedimiento para realizar la resta

    resta = numero_1 - numero_2
    print("El resultado de la resta es", resta)



def ej2():
    # Ejercicios de práctica numérica

    # Operadores con números decimales
    # Ahora los valores a operar deben ser ingresados por
    # consola con la función "input" como se ve a continuación
    print('Ingrese el primer número decimal a operar:')
    numero_1 = int(input())

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = int(input())

    # Alumno: Imprima en pantalla los dos números decimales solicitados
    # print(....)
    print('Los dos números decimales solicitados son:',numero_1,"y",numero_2)

    # Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
    suma = numero_1 + numero_2 # Suma
    resta = numero_1 - numero_2 # Resta
    division = numero_1 % numero_2 # División
    multiplicacion = numero_1 * numero_2 # Multiplicación



    # numero_1, numero_2
    # Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
    print("El resultado de sumar",numero_1, "y", numero_2, "es", suma)
    print("El resultado de restar",numero_1, "y", numero_2, "es", resta)
    print("El resultado de multiplicar",numero_1, "y", numero_2, "es", multiplicacion)
    print("El resultado de dividir",numero_1, "y", numero_2, "es", division)
     
    # El resultado de sumar 4 y 2 es 6

def ej3():
    # Ejemplos variables de texto

    # Ingrese primero su nombre y luego su apellido
    # Capture ambos datos e imprima su nombre completo
    print('Ingrese su nombre/s:')
    nombre = str(input())

    print('Ingrese su apellido/s:')
    apellido = str(input())

    # Imprima su nombre completo
    nombre_completo = nombre + " "+ apellido
    print("Mi nombre es", nombre_completo)
    # Almacenar su nombre completo en una variable
    
    # nombre_completo = .....

    # Imprimir la cantidad de letras que posee su nombre completo
    print("Mi nombre completo posee", len(nombre_completo)-1, "letras")
    print("Mi nombre completo posee", len(nombre) + len(apellido), "letras")

def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    # De cada palabra debe tomar la primera letra y armar el acrónimo
    palabra_1_init= palabra_1[0]
    palabra_2_init= palabra_2[0]
    palabra_3_init= palabra_3[0]
    print(palabra_1_init, palabra_2_init, palabra_3_init)
    print(palabra_1_init + palabra_2_init + palabra_3_init)

    # Ejemplo: Alumbrado, barrido y limpieza --> ABL
    # Imprimir el resultado en pantalla


def ej5():
    # Ejemplos variables de texto

    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    palabra_1_init= palabra_1[:3]
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    palabra_2_fin= palabra_2 [-3:]
    # Formar una nueva palabra con los recortes solicitados
    nueva_palabra = palabra_1_init + palabra_2_fin
    # Imprima en pantalla los resultados
    print(nueva_palabra)


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
