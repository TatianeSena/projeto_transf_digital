#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem
#cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

viagem=float(input('Digite o km da viagem km/h '))
if viagem<=200:
    print('O Preço da sua passagem foi de {}.'.format(viagem*0.50))
else:
    print('O preço da sua passagem foi de {}'.format(viagem*0.45))
