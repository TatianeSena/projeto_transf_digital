#desafio 11 Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m**2

l=float(input('digite a largura'))
a= float(input('digite a altura'))
p= l*a
d= p*2
t= d/2
print('A parede de {}, tem {} altura e {} largura, será necessário {} litros de tinta.'.format(p, a, l, ('%.2f'%t)))
