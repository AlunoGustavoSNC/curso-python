# 6) Faça um programa que leia 5 números e informe o maior número.

n = []

for i in range(0, 5):
    n.append(int(input(f'Digite o número {i+1}: ')))

n.sort(reverse=True)

print(f'O maior número é {n[0]}')