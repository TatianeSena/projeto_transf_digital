# desafio 10 Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar.

real = float(input('valor na carteira'))
cotacao = float(input('Informe o valor da cotação do dólar: R$ '))
conversao = real / cotacao
print('A quantidade de dólar que é possível comprar é de R$', ('%.2f' % conversao))

# ou

# real=float(input('valor na carteira'))
# dolar= real/'valor da cotacão'
# print('Com R${} você pode comprar US${}'.format(real, dolar))
