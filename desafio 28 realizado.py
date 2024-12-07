#Escreva um programa que faça o computador 'pensar' um número inteiro entre 0 e 5 e peça
#para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

usuário=int(input('Digite um número: '))
import random
s=random.choice([0, 1, 2, 3, 4, 5])
print('O número escolhido foi {}.'.format(s))
if usuário==s:
    print('você ganhou!!!')
else:
    print('você perdeu!!')
