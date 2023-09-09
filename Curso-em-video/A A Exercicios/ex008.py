# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = float(input('Escreva a quantidade de metros: '))

cm = m * 100

mm = cm * 10

print('Em metros:', m)
print('Em centímetros:', cm)
print(f'Em milímetro: {mm}')