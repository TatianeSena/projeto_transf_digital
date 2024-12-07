#desafio 19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
#nome deles e escrevendo o nome do escolhido.

import random
al1= str(input('nome do aluno 1: ')
al2= str(input('nome do aluno 2: ')
al3= str(input('nome do aluno 3: ')
al4= str(input('nome do aluno 4: ')
s=random.choice([al1, al2, al3, al4])
print('O aluno sorteado para limpar o quadro foi', s)
     
