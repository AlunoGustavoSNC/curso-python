# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

caracter = input('Escreva um número, palavra ou caracter: ')

print('É um número? ', caracter.isnumeric())
print(f'É um número decimal? {caracter.isdecimal()}')
print(f'É uma letra? {caracter.isalpha()}')