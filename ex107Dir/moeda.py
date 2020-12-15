def aumentar(v, p):
    """
    Aumenta o valor de acordo com a porcentagem.
    :param v: O valor original.
    :param p: A porcentagem a ser aumentada.
    :return: O valor aumentado.
    """
    if p < 0:
        p *= -1
    aumento = 1 + p / 100
    valor = v * aumento
    return valor


def diminuir(v, p):
    """
    Diminui o valor de acordo com a porcentagem.
    :param v: O valor original.
    :param p: A porcentagem a ser reduzida.
    :return: O valor reduzido.
    """
    if p < 0:
        p *= -1
    if p > 100:
        p = 100
    aumento = 1 - p / 100
    valor = v * aumento
    return valor


def dobro(v):
    """
    Dobra o valor recebido.
    :param v: valor a ser dobrado.
    :return: valor dobrado.
    """
    return v * 2


def metade(v):
    """
    Corta o valor recebido pela metade.
    :param v: valor a ser reduzido.
    :return: metade do valor.
    """
    return v * 0.5
