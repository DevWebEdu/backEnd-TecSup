# ejemplo
# Para evitar que en cada impresion se ejecute una nueva linea, se puede agregar el parametro end y este indicara como queremos que actue al finalizar la linea
# for numero in range(5):
#     print(numero, end="")



# EJERCICIO 1
# Escriba el codigo que le pida al usuario ingresar la altura y el ancho de un rectangulo y
# que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# altura=int(input("Altura: "))
# ancho=int(input("Ancho: "))

# for h in range (altura):
#     for w in range (ancho):
#         print('*',end="")
#     print("")

# EJERCICIO 2
# Escribir el codigo que el usuario le ingrese el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****


# EJERCICIO 3
# De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo
# invertido
# Ejemplo
# Altura: 4
# Altura=4
# while (Altura > 0):
#     for h in range(Altura):
#         print("x", end="")
#     print("")
#     Altura -=1
    




# EJERCICIO 4
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 12

# numero_ingresado = int(input("Ingresa un numero ** Serie Collatz ** :"))


# while numero_ingresado > 1:
#     if(numero_ingresado % 2 == 0 ):
#         numero_ingresado = numero_ingresado/2 
#     else:
#         numero_ingresado = numero_ingresado*3 + 1

#     print(numero_ingresado, end=" ")
# print("")



# EJERCICIO 5
# si el texto de ingreso es:
texto = "hola alumnos buenas noches ya se viene el break"
# entonces el texto resultado debera ser:

# Hacer el codigo para ello

# texto_destructurado = texto.split(" ")
# for palabra_indice in range(len(texto_destructurado)):
#     texto_destructurado[palabra_indice] = texto_destructurado[palabra_indice].capitalize()


# print(texto_destructurado)

# EJERCICIO 6
# ingresar numeros hasta que ese numero sea adivinado
numero_adivinar = 10
# 5 => 'el numero es mayor que ese'
# 13 => 'el numero es menor que ese'
# 10 => 'felicidades adivinaste el numero'


# EJERCICIO 7
# dado los siguientes numeros:
numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
# indicar cuantos de ellos son multiplos de 3 y de 5 , ademas si hay un multiplo de 3 y de 5 no contabilizarlos
# multiplos de 3: 3 , multiplos de 5: 1