# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

p = float(input('Digite o preço do produto: '))

print('O preço do produto é R${:.2f}, Com 5 porcento de desconto o preço seria R${:.2f}' .format(p, p * 0.95))