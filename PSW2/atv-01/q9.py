# 9) Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

n = []

for i in range(0, 10):
    n.append(float(input(f'Digite o número {i+1}: ')))

n.sort(reverse=True)

print(n)