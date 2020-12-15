# Crie um função escreva que mostre 2 linhas com tamanho adaptável e no meio a mensagem
def escreva(texto):
    tamanho = len(texto) + 4
    print('-' * tamanho)
    print(' ', texto)
    #print(f'  {texto}')
    print('-' * tamanho)


# main
escreva('Olá Mundo!')
escreva('Texto incrivelmente grande mas as linhas acompanham!')
escreva('123')
