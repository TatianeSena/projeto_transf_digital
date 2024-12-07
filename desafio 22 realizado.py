#desafio 22 - Crie um programa que leia o nome completo de uma pessoa
#e mostre:
#    -o nome com todas as letras maiusculas
#    -o nome com todas minusculas
#    -quantas letras ao todo (sem considerar espaços).
#    -Quantas letras tem o primeiro nome.

nome=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nom em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa= nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
