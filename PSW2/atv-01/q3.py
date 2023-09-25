# 3) Faça um Programa que leia três números e mostre-os em ordem decrescente.

n = []

n.append(int(input('Digite o primeiro número: ')))
n.append(int(input('Digite o segundo número: ')))
n.append(int(input('Digite o segundo número: ')))

n.sort(reverse=True)

print(n)