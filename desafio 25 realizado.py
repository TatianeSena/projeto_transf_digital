#desafio - 25 - Crie um programa que leia o nome de uma pessoa
#e diga se ela tem 'silva' no mome.

nome= str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
