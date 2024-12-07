#Escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

velocidade=float(input('Qual a velocidade:  km/h'))
excedente=(velocidade-80)*7
if velocidade>80:
    print('Você foi multado!')
    print('A sua multa foi de R$ {}.'.format(excedente))
else:
    print()
