edad_roberta = 20

if edad_roberta >=18:
    print('si se puede entrar a la discoteca')
else:
    print('no puedes entrar a la discoteca')


edad_martin = 70
if edad_martin >= 65: 
    print('esta persona esta jubilada')
elif edad_martin >= 18:
    print('Esa persona es mayor de edad')
elif edad_martin>=0:
    print('Esa persona es menor de edad')
else: 
    print('Edad imposible')


#la forma para ingresar valores al programa desde una consola 
data = int(input("Hola, ingresa tu nombre : "))
print(type(data))
print(data+10)

# Dependiendo de la talla del polo podriamos hacer lo siguiente : si es XL entonces indicar que llegara a fin de mes, si  L o M el color del polo , si es S indicar que solamente hay en color morado , si ingresa otra cosa indicar que la talla es incorrecta 

talla = input("Que talla de polo desea : ")
if(talla=='XL' or  talla=="xl"):
    print('El polo en {} llegara a fin de mes'.format(talla))
elif(talla=='L' or talla=='M'):
    talla_L_M = input("Que color de polo desea : ")
    print('Su polo es de talla {} y es de color {}'.format(talla,talla_L_M))
elif(talla=='S' or talla=='s'):
    print('en la talla {} solo existe en color Morado'.format(talla))
else:
    print("Talla Inexistente")