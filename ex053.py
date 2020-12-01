# pegue uma frase e diga se é um palíndromo
frase = input('Digite uma frase: ').strip().lower()
frase = ''.join(frase.split())
erro = -1
for i in range(0, len(frase)):
    j = len(frase) - 1 - i
    # print(frase[i], '     ', frase[j])
    if frase[i] != frase[j] and erro == -1:
        erro = i
if erro == -1:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palindromo.')
    letraNormal = frase[erro]
    letraInvertida = frase[(len(frase) - 1) -erro]
    print('Na posição {}, a letra é "{}", mas ao contrario a letra é "{}"'.format(erro+1,letraNormal,letraInvertida))
# inverso = ''
# for i in range(len(frase)-1, -1, -1:
#   inverso += frase[i]
# inverso += frase[::-1]
# if inverso == frase



