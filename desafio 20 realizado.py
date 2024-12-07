#desafio 20 - O mesmo professor do desafio anterior quer sortear a ordem de apesentação de trabalhos dos alunos. Faça
#um programa qe leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
al1= input('Nome do aluno')
al2= input('Nome do aluno')
al3= input('Nome do aluno')
al4= input('Nome do aluno')
lis=(al1, al2, al3, al4)
s= random.sample(lis, 4)
print('A ordem que foi sorteada é', s)
