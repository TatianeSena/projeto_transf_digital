#Faça um programa que leia três números e mosrtre qual é o maior e  qual é o menor.

n1=int(input('Digite um número: '))
n2=int(input('Digite um número: '))
n3=int(input('Digite um número: '))
lista=[n1, n2, n3]
print('O maior número digitado foi: {}'.format(max(lista)))
print('O menor número digitado foi: {}'.format(min(lista)))
