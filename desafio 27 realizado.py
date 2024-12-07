#desafio 27 - faça um programa que leia o nome completo de uma
#pessoa, mostrando em seguida o primeiro e o último nome
#separadamente.
#     ex. Ana Maria de Souza
#     primeiro=Ana
#     ultimo-Souza

n= str(input('Digite seu nome completo: ')).strip()
separa= n.split()
print('Primeiro nome: {}'.format(separa[0]))
print('Último nome: {}'.format(separa[len(separa)-1]))
