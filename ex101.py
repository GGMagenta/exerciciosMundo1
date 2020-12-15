# Crie uma função voto que recebe o ano de nascimento e retorna o valor literal
# Negado, Opcional ou Obrigatório
from datetime import datetime


def voto(ano):
    """
    Calcula se o voto é obrigatório, opcional, ou não pode votar
    :param ano: Ano de nascimento
    :return: obrigatório, opcional ou negado dependendo da idade
    """
    # from datetime import datetime
    # pode importar somente para a função
    anoAtual = datetime.today().year
    idade = anoAtual - ano
    resultado = 'Sua idade é '+str(idade)
    # resultado = f'Sua idade é {idade}'
    # string formatada ou format() funciona fora do print, é uma função da str
    if idade < 16:
        resultado += ', não pode votar.'
    elif 18 <= idade < 65:
        resultado += ', o voto é obrigatório.'
    else:
        resultado += ', o voto é opcional.'
    return resultado


#main
nascimento = int(input('Informe o ano de nascimento: '))
print(voto(nascimento))