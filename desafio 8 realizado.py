# desafio 8 Escreva um programa qu leia um valor em metros e o exiba
# convertido em centimetros e milimetros.

n = float(input('valor em metro; '))
dm = n * 10
c = n * 100
mm = n * 1000
km = n * 000.1
hm = n * 00.1
dam = n * 0.1

print('\033[4;47m', n, ' metro equivale a,', dm, ' decímetro.\033[m')
print('\033[4;41m', n, ' metro equivale a,', c, ' centímetros.\033[m')
print('\033[4;42m', n, ' metro equivale a, ', mm, ' milímetros.\033[m')
print('\033[4;43m', n, ' metro equivale a, ', dam, ' decametro.\033[m')
print('\033[4;44m', n, ' metro equivale a, ', hm, ' hectometro.\033[m')
print('\033[4;45m', n, ' metro equivale a, ', km, ' kilometro.\033[m')
