#4) Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V- Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('Responda M para Matutino, V para Vespertino ou N para Noturno \n')
turno = input('Em qual turno você estuda? ')

if turno == 'M':
    print('Bom dia!!!')
elif turno == 'V':
    print('Boa tarde!!!')
elif turno == 'N':
    print('Boa noite!!!')
else:
    print('Valor inválido!')