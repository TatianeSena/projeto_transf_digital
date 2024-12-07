#desafio 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo, calcule
#e mostre o comprimento da hipotenusa.

import math
a=int(input('digite um número: '))
b=int(input('digite um número: '))
hipo= math.hypot(a,b)
print('um trinagulo retangulo tem {} cateto oposto e {} cateto adjacente, o comprimento da hipotenusa é {}.'.format(a, b, hipo))
