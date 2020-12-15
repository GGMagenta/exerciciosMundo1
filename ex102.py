# criar função fatorial que calcula o fatorial de um número
# com um valor opcional show que vai mostrar ou não resolvendo na tela
from time import sleep


def fatorial(numero, show=False):
    """
    calcula fatorial
    :param numero: número a ser calculado
    :param show: se vai mostrar na tela a conta inteira
    :return: fatorial de n
    """
    n = numero
    resultado = 1
    frase = ''
    while n > 0:
        resultado *= n
        if show:
            frase += str(n)
            if n > 1:
                frase += ' x '
            else:
                frase += ' = '
        n -= 1
    frase += str(resultado)
    return frase

# main
print(fatorial(5, show=True))