# 7) Faça um programa que leia 5 números e informe a soma e a média dos números.

n = []
soma = 0

for i in range(0, 5):
    n.append(int(input(f'Digite o número {i+1}: ')))

    soma += n[i]

print(f'\nA soma dos valores é {soma}')
print(f'A média dos valores é {soma / len(n)}')