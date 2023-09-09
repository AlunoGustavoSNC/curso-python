# Desenvolva um programa que leia as duas notas de um aluno e calcule a sua média

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

print('\n' + '='*30, '\n')

print(f'Sua média é', end=' ')
print((n1 + n2)/2)