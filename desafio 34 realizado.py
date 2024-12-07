#Escreva um programa que pergunte  salário de um funcionario e calcule o valor do seu
#aumento.
#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%.

salario= float(input('salário:R$ '))
if salario>=1250:
    print('Para salário de {}, o aumento foi de {}'.format(salario, salario*10/100+salario))
else:
    print('Para salário de {}, o aumento foi de {}'.format(salario, salario*15/100+salario))

