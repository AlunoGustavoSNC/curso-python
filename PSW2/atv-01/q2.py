#2) Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamArquivo = float(input('Tamanho do arquivo (em MegaBytes): '))
velocidade = int(input('Velocidade da internet (em MegaBits por segundo): '))

tamArqBits = tamArquivo * 8

tempoDownload = (tamArqBits / velocidade)

print('O tempo de download será de {:.0f} segundos' .format(tempoDownload))