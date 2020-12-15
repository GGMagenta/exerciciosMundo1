def aumentar(v, p, f=False):
    """
    Aumenta o valor de acordo com a porcentagem.
    :param v: O valor original.
    :param p: A porcentagem a ser aumentada.
    :param f: Se vai ser formatado pela função Moeda
    :return: O valor aumentado.
    """
    if p < 0:
        p *= -1
    aumento = 1 + p / 100
    valor = v * aumento
    if f:
        return moeda(valor)
    else:
        return valor


def diminuir(v, p, f=False):
    """
    Diminui o valor de acordo com a porcentagem.
    :param v: O valor original.
    :param p: A porcentagem a ser reduzida.
    :param f: Se vai ser formatado pela função Moeda
    :return: O valor reduzido.
    """
    if p < 0:
        p *= -1
    if p > 100:
        p = 100
    aumento = 1 - p / 100
    valor = v * aumento
    if f:
        return moeda(valor)
    else:
        return valor


def dobro(v, f=False):
    """
    Dobra o valor recebido.
    :param v: valor a ser dobrado.
    :param f: Se vai ser formatado pela função Moeda
    :return: valor dobrado.
    """
    if f:
        return moeda(v * 2)
    else:
        return v * 2


def metade(v, f=False):
    """
    Corta o valor recebido pela metade.
    :param v: valor a ser reduzido.
    :param f: Se vai ser formatado pela função Moeda
    :return: metade do valor.
    """
    if f:
        return moeda(v * 0.5)
    else:
        return v * 0.5


def moeda(v):
    """
    Pega um valor e mostra na formatação de moeda.
    :param v: valor a ser formatado.
    :return: valor formatado em reais R$
    """
    valor = f'R${v:.2f}'
    valor = valor.replace('.', ',')
    return valor


def resumo(v, a, r):
    """
    Mostra uma tabela com o dobro, metade, aumento e redução do valor
    :param v: valor original para o cálculo
    :param a: porcentagem de aumento
    :param r: porcentagem de redução
    :return: Nada, apenas um print com as informações
    """
    print('=' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('=' * 30)
    print(f'{"Valor analizado:":<20}{moeda(v):<10}')
    print(f'{"Dobro do valor:":<20}{dobro(v, True):<10}')
    print(f'{"Medade do valor:":<20}{metade(v, True):<10}')
    print(f'{"Aumento de "}{str(a)+"%:":<9}{aumentar(v, a, True):<10}')
    print(f'{"Redução de "}{str(r)+"%:":<9}{diminuir(v, r, True):<10}')
