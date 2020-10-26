#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Ignacio Melchiori"
__email__ = "melchiorignacio@gmail.com"
__version__ = "1.3"


def ej1():
    # Ejercicios de práctica con números
    print('Nuestra primera calculadora')
    print('Ingrese los números con los que desea operar')
    numero_1 = float(input())
    numero_2 = float(input())

    sumar = numero_1 + numero_2
    restar = numero_1 - numero_2
    multiplicar = numero_1 * numero_2
    dividir = numero_1 % numero_2
    potenciar = numero_1 ** numero_2

    print('La suma entre', numero_1, 'y', numero_2, 'es', sumar)
    print('La resta entre', numero_1, 'y', numero_2, 'es', restar)
    print('La multiplicacion entre', numero_1, 'y', numero_2, 'es', multiplicar)
    print('La division entre', numero_1, 'y', numero_2, 'es', dividir)
    print( numero_1, 'elevado a', numero_2, 'es', potenciar)
    
    '''
    Realice un calculadora, se ingresará por línea de comando dos
    números reales y se deberá calcular todas las operaciones entre ellos:
    - Suma
    - Resta
    - Multiplicación
    - División
    - Exponente/Potencia
  
    - Para todos los casos se debe imprimir en pantalla el resultado aclarando
      la operación realizada en cada caso y con que números
      se ha realizado la operación
      ej: La suma entre 4.2 y 6.5 es 10.7

    '''


def ej2():
    print('Ejercicios de práctica numérica y cadenas')
    print("Por favor ingrese su nombre")
    nombre = str(input())
    print("Ahora ingrese su apellido")
    apellido = str(input())
    nombre_completo = nombre +" " + apellido 
    print("Ingrese su número de DNI")
    dni = str(input())
    print("ingrese su edad")
    edad = int(input())
    print("ingrese su altura en cm")
    altura = int(input())

    print("Su nombre completo es",nombre_completo, "su DNI es", dni, "su edad", edad, "y altura", altura, "cm")
    '''
    Realice un programa que consulte por consola:
    - El nombre completo de la persona
    - El DNI de la persona
    - La edad de la persona
    - La altura de la persona
  
    Finalmente el programa debe imprimir dos líneas de texto por separado
    - En una línea imprimir el nombre completo y el DNI, aclarando de que
      campo se trata cada uno
            Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
    - En la segunda línea se debe imprimir el nombre completo, edad y
      altura de la persona
      Nuevamente debe aclarar el campo de cada uno, para el que lo lea
      entienda de que se está hablando.

    '''


def ej3():
    print('Ejercicios de práctica con cadenas')
    print("por favor ingrese el nombre completo de su padre")
    padre_1 = str(input())
    print("por favor ingrese el nombre completo de sus madre")
    padre_2 = str(input())
    
    nombre_padre_1, apellido_padre_1 = padre_1.split(' ')
    nombre_padre_2, apellido_padre_2 = padre_2.split(' ')

    print("por favor ingrese su nombre")
    hijo = str(input())
    print("Su nombre es", hijo, apellido_padre_1, apellido_padre_2)


    '''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus

    '''


def ej4():
    # Ejercicios de práctica con cadenas
    print('Comencemos a ponernos serios')
    print("ingrese el nombre y apellid de una persona")
    persona_1 = str(input())
    
    print("ingrese el nombre y apellid de una persona")
    persona_2 = str(input())
    nombre_persona_2, apellido_persona_2 = persona_2.split(" ")
    
    son_parientes = apellido_persona_2 in persona_1
    print(persona_2, 'es pariente de', persona_1,'?', son_parientes)

    '''
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    '''


def ej5():
    # Ejercicios de práctica con cadenas
    print('Ahora si! buena suerte!')
    print("Por favor ingrese su nombre completo")
    nombre_compelto = str(input())

    print('Su nombre en minusculas es:',nombre_compelto.lower())
    print('Su nombre en mayusculas es:',nombre_compelto.upper())
    nombre , apellido = nombre_compelto.split(" ")
    print(nombre.capitalize(), apellido.capitalize())

    '''
    Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''


if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
