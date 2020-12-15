# Crie uma funcao area pegando largura e altura do terreno e mostrando a area
def calcularArea(lar, com):
    area = lar * com
    print(f'A Área do terreno de {lar}m x {com}m é {area}M².')


# main
largura = float(input('Digite a largura do terreno em metros: '))
comprimento = float(input('Digite o comprimento do terreno em metros: '))
calcularArea(largura, comprimento)