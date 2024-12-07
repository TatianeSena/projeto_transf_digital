#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
#podem ou não formar um triângulo.

a= float(input('Primeiro lado: '))
b= float(input('Segundo lado: '))
c= float(input('Terceiro lado: '))
if (a +b < c) or (a + c < b) or (b + c < a):
    print('É um triangulo')
else:
    print('Não é um triangulo')
