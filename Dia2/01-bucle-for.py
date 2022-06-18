numeros = [ 10,20,30,40,50,60]

for numero in numeros : 
    print( numero)

frase_motivadora = 'al que madruga , encuentra todo cerrado'
contador_n=0
#Codigo para decifrar cuantas n  existen en el String frase_motivadora
for caracter in  frase_motivadora:
    if(caracter=='n'):
        contador_n += 1
        print("se encontraron {} n's".format(contador_n))


for valor in range(4,7,2):
    print(valor)


for valor in range(2,10):
    print(valor)


numero=[10,30,12,17,24,67]
numeros_pares_total=0
numeros_multiplos=0
for number in numero:
    if(number%2==0):
        print("El {} es par".format(number))
        numeros_pares_total+=1
    if(number%3==0):
         print("El {} es multiplo de 3".format(number))
         numeros_multiplos+=1
    else:
        print("El {} no cuenta".format(number))

print("numero pares{}".format(numeros_pares_total))
print("numero multiplos de 3  {}".format(numeros_multiplos))