#desafio 9 Faça um programa que leia um número inteiro na tela e mostre a
#tela a sua tabuada.

#numero=int(input('Qual tabuada você quer saber? Digite de 1 a 10.\n'))
#print('tabuada do', numero, ':\n')
#for i in range(1, 11):
#    print('\033[7;40m', numero, 'x', i,'=', numero*i, '\033[m\n')

#ou

num=int(input('Digite um número para ver sua tabuada; '))
print('\033[1m{} x {} = {}\033[m'.format(num, 1, num*1))
print('\033[1;31m{} x {} = {}\033[m'.format(num, 2, num*2))
print('\033[1;32m{} x {} = {}\033[m'.format(num, 3, num*3))
print('\033[1;33m{} x {} = {}\033[m'.format(num, 4, num*4))
print('\033[1;34m{} x {} = {}\033[m'.format(num, 5, num*5))
print('\033[1;35m{} x {} = {}\033[m'.format(num, 6, num*6))
print('\033[1;36m{} x {} = {}\033[m'.format(num, 7, num*7))
print('\033[1;37m{} x {} = {}\033[m'.format(num, 8, num*8))
print('\033[1;31m{} x {} = {}\033[m'.format(num, 9, num*9))
print('\033[1;32m{} x {} = {}\033[m'.format(num, 10, num*10))
