# Crie outra 3x3 com valores lidos do teclado, e mostre
# a soma dos valores pares, soma da terceira coluna e o maior valor da 2 coluna
matriz = []
for l in range(0, 3):
    linha = []
    for c in range(0, 3):
        n = int(input(f'Digite um número para [{l}, {c}]: '))
        linha.append(n)
    matriz.append(linha[:])
    linha.clear()
somaPares = 0
soma3 = 0
maior2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = matriz[l][c]
        print(f'[{n}]', end='')
        if n % 2 == 0:
            somaPares += n
        if l == 1:
            if c == 0:
                maior2 = n
            elif n > maior2:
                maior2 = n
        if c == 2:
            soma3 += n
    print('')
print(f'A soma de todos os números pares é: {somaPares}')
#  for l in range(0, 3) soma3 += matriz[l][2]
print(f'A soma de todos os números da coluna 3 é: {soma3}')
#  for c in range(0, 3) if matriz[1][c] > maior: maior2 = matriz[1][c]
print(f'O maior número da linha 2 é: {maior2}')
