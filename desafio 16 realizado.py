#desafio 16 - Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
#ex. digite um número: 6.127
#o número 6.127 tem a parte inteira 6.

import math
num= float(input('digite um número: '))
inteiro= math.trunc(num)
print('O número {} tem sua parte inteira {}.'.format(num, inteiro))
