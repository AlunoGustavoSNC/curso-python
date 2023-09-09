# Faça um algoritmo que leia o salário de um funcioanrio e mostre seu novo salário com 15% de aumento

s = float(input('Digite o valor do seu salário em real: '))

print('Seu salário é R${:.2f}, com reajuste de 15 porcento ele passa a ser R${:.2f}' .format(s, s * 1.15))