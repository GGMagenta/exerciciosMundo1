# Crie um matriz 3x3 com valores lidos do teclado, e mostre na formatação correta
matriz = []
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    linha = []
    for c in range(0, 3):
        n = int(input(f'Digite um número para [{l}, {c}]: '))
        linha.append(n)
    matriz.append(linha[:])
    linha.clear()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print('')