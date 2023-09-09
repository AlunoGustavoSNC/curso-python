# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m^2

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))

m2 = l * a

tinta = m2 / 2

print('A parede tem', m2, 'metros quadrados', end=' ')
print(f'e é necessário {tinta} litros de tinta para pinta-la')