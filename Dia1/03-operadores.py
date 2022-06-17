#Operadores Aritmeticos
edad_juan =40
edad_maria=34
#Suma
print(edad_juan+edad_maria)
#Resta
print(edad_juan-edad_maria)
#Multiplicacion
print(edad_juan*edad_maria)
#division
print(edad_juan/edad_maria)
#Modulo resultado entero de la division 
print(edad_juan%edad_maria)
#Cociente
print(edad_juan//edad_maria)


#Operadores de  Comparacion

edad_luis=15
edad_martha=30


#>Mayor que
print (edad_luis > edad_martha)
#< Menor que
print(edad_luis > edad_martha)
# == igual que 
print(edad_luis == edad_martha)
# != diferente que
print(edad_luis != edad_martha)
#and Y
print (edad_luis > 18 and edad_luis > edad_martha)
#or  O
print (edad_luis > 18 or edad_luis > edad_martha)
#not NO
print (not edad_luis > 50)



#Ejercicios 
edad_eduardo=18
edad_renato=26
edad_laura=35

# Como saber si eduardo es mayor de edad
print(edad_eduardo >= 18)
# Como saber si eduardo es mayor que laura
print(edad_eduardo > edad_laura)
# Como saber si renato es menor que laura pero mayor que eduardo
print(edad_renato<edad_laura and edad_renato>edad_eduardo)
# como saber si laura puede ser mayor que renato o menor que eduardo
print(edad_laura>edad_renato or edad_laura < edad_eduardo)

#Operadores de Asignacion
# = asignacion
edad = 50
# += Incremento
edad += 1
# -= Decremento
edad -= 1
# *= Multiplicador
edad *= 1
# /=division
edad /= 2 