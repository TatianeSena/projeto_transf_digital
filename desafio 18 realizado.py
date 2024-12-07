#desafio 18 - Faça um programa que leia um ângulo qualquer e mostre na tela o
#valor do seno, cosseno e tangente desse ãngulo.

import math
     Ãngulo= float(input('Digite o Ãngulo que você deseja; '))
     seno= math.sin(math.radians(ângulo))
     print('o ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
     cosseno= math.cos(math.radians(ângulo))
     print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))
     tangente= math.tan(math.radians(ângulo))
     print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))
