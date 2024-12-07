#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date
ano=int(input('Ano: '))
if ano==0:
    ano=date.today().year
if (ano%4==0):
    print('Bissexto')
else:
    print('Não é bissexto')
