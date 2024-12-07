#desafio 4 Faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas a informações possíveis sobre ele.

n=input('digite um valor; ')
print('\033[1;33mO tipo primitivo desse valor é\033[m', '\033[4m', type(n),'\033[m')
print('\033[1;34mÉ um número?\033[m','\033[7;40m', n.isnumeric(),'\033[m')
print('\033[1;35mSó tem espaços?\033[m','\033[4m', n.isspace(), '\033[m')
print('\033[1;36mÉ alfabético?\033[m','\033[47m', n.isalpha(), '\033[m')
print('\033[1;31mÉ alfanúmerico?', n.isalnum(), '\033[m')
print('\033[1;32mEstá em maiúscula?\033[m','\033[4m', n.isupper(), '\033[m')
print('\033[1;33;40mEstá em minúscula?\033[m','\033[7m', n.islower(), '\033[m')
print('\033[1;36;7mEstá capitalizada?\033[m','\033[7;40m', n.istitle(), '\033[m')

      
