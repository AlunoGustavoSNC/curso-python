#1) Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#a. Para homens: (72.7*h) - 58
#b. Para mulheres: (62.1*h) - 44.7 (h = altura)
#c. Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.

peso = float(input('Informe seu peso (em kg): '))
alt = float(input('Informe sua altura (em metros): '))
sexo = input('Informe o seu sexo (M para masculino e F para feminino): ')

if sexo == 'M' or sexo == 'm':
    pesoIdeal = (72.7 * alt) - 58
    print('O seu peso ideal é {:.2f}kg' .format(pesoIdeal))

    if pesoIdeal > peso:
        print('Você está {:.2f}kg abaixo do peso' .format(pesoIdeal - peso))
    elif pesoIdeal < peso:
        print('Você está {:.2f}kg acima do peso' .format(peso - pesoIdeal))
    else:
        print('Você está com o peso ideal')

elif sexo == 'F' or sexo == 'f':
    pesoIdeal = (62.1 * alt) - 44.7
    print('O seu peso ideal é {:.2f}kg' .format(pesoIdeal))

    if pesoIdeal > peso:
        print('Você está {:.2f}kg abaixo do peso' .format(pesoIdeal - peso))
    elif pesoIdeal < peso:
        print('Você está {:.2f}kg acima do peso' .format(peso - pesoIdeal))
    else:
        print('Você está com o peso ideal')