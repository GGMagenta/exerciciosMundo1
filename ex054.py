# Pegue 7 datas de nascimento e diga quantas são maiores de idade
#  considerar maior idade = 21
from datetime import date
maiores = 0
menores = 0
anoAtual = date.today().year
for i in range(0, 7):
    ano = int(input('Qual o ano de nascimento? '))
    idade = anoAtual - ano
    # print(idade)
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print('Dessas pessoas, {} são maiores de idade e {} são menores de idade.'.format(maiores,menores))
