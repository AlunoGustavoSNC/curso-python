# OPERADORES ARITMÉTICOS

# SOMA +
# Subtração -
# Divisão /
# Multiplicação *

# Potência **
# Resto %

# -----------------------------------------------------------

print("\nCalculo de Densidade do solo\n")

mostra_seca = int(input("escreva a mostra seca (em gramas): "))
volume_total = int(input("escreva o volume total (em cm^3): "))
densidade_particula = 2.65

densidade_solo = mostra_seca / volume_total

porosidade_total_solo = (1 - (densidade_solo / densidade_particula)) * 100 

print("A densidade total do solo é de {:.2f} g/cm^3\n" .format(densidade_solo))

print("----------------------------------------------------")
print("\n A Porosidade total do solo é de {:.2f}%" .format(porosidade_total_solo))

