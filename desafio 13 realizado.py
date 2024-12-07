#desafio 13 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sl= float(input('salário: R$ '))
reaj= sl*15/100
nsl= sl+reaj
print('salário: R$', sl)
print(' Reajuste do salário: R$', reaj)
print('novo salário: R$', nsl)
