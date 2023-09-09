# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quanto dólares ela pode comprar

real = float(input('Quantos reais você tem? '))

dolar = real / 5.22

print('Com R${:.2f}, você pode comprar ${:.2f}' .format(real, dolar))