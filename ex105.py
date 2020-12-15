# Crie uma função notas que leia varias notas e retorne um dicionario
# quantidade de notas, maior e menor nota, média da turma e situação(opcional)
def notas(*notas, situacao=False):
    """
    Pega varias notas e calcula q quantidade, maior e menor, média e informa a situação
    :param notas: todas as notas
    :param situacao: Informa a situação de acorde com a média
    :return: dicionário com as informações
    """
    maior = menor = media = 0
    for i, v in enumerate(notas):
        if i == 0:
            maior = menor = v
        if v > maior:
            maior = v
        elif v < menor:
            menor = v
        media += v
    media /= len(notas)
    dic = {}
    dic['total'] = len(notas)
    dic['maior'] = maior  # max(notas)
    dic['menor'] = menor  # min(notas)
    dic['media'] = media  # sum(notas)/len(notas)
    if situacao:
        if media >= 7:
            dic['situacao'] = 'Boa'
        elif media >= 5:
            dic['situacao'] = 'Rasoável'
        else:
            dic['situacao'] = 'Ruim'
    return dic


# main
resp = notas(3, 9, 8.5, 4, 7, situacao=True)
print(resp)