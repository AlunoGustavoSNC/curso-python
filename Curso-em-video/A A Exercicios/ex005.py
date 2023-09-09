# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e antecessor

n = int(input('Digite um  número: '))

print(f'O número é {n}', end=' >>> ')
print(f'O número antecessor a essse é {n-1}', end=' >>> ')
print(f'O número sucessor a essse é {n+1}')