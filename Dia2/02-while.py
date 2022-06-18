#while
numero =10
while numero > 0:
    print('numero positivo')
    print(numero)
    numero -=1

#do while  no existe en python

#solicitar 5 digitos para la loteria pero estos no pueden ser mayores que 100 ni numeros negativos

contador_loteria=0
while contador_loteria < 5:
    digito_loteria=int(input("ingrese un digito numero  {} :".format(contador_loteria)))
    contador_loteria+=1
    if(digito_loteria>100):
        print("solo se solicita numeros menores que  100")
        continue
    if(digito_loteria<0):
        print("solo se solicita numeros mayores que 0")
        continue
    print("tu numeros son {}".format(digito_loteria))