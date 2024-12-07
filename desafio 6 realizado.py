#desafio 6 Crie um algoritmo que leia um número e mostre o seu dobro,
#triplo e raiz quadrada.

n=int(input('digite um valor: '))
a=n*2
b=n*3
c=n**(1/2)
#print('\033[34;47mo dobro de {} é {}, o triplo é {} e a raiz quadrada é {}\033[m'.format(n, a, b, c))
print('\033[7;45mo dobro de {} vale {}.\033[m'.format(n, (n*2)))
print('\033[1;30;41mo triplo de {} vale {}\033[m. \n\033[4;33;40mA raiz quadrada de {} é igual a {}.\033[m'.format(n, n*3, n, (n**(1/2)))) #ou pow(n, (1/2)
