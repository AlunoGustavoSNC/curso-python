# 10) Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve serarmazenado). Após esta entrada de dados, faça:
# a. Mostre a quantidade de valores que foram lidos;
# b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;

n = []
c = 0
i = 0

print('\nDigite suas notas\n')

while c != -1:
    n.append(int(input(f'Digite a nota {i+1}: ')))

    if n[i] == -1:
        c = -1
        n.pop(i)
    elif n[i] < 0 or n[i] > 100:
        print('Valor inválido, por favor digite um número entre 0 e 100')
        n.pop(i)

    i += 1

print(f'A quantidade de notas é {len(n)}')
print(f'Os valores são {n}')

n.reverse()

print(f'Os valores reordenados são:')

for i in range(0, len(n)):
    print(n[i])

print('\nPrograma encerrado')
