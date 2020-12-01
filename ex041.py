# Pegue o ano de nascimento e calcule a classe de acordo com a idade
# ate 9 - mirim  ate 14 - infantil  ate 19 - junior  ate 25- senior  acima - master
from datetime import date
ano = int(input('Informe o ano do seu nascimento: '))
anoAtual = date.today().year
idade = anoAtual-ano
print('Você tem {} anos. '.format(idade) , end='')
if idade<9:
    print('Sua categoria é mirim.')
elif idade<14:
    print('Sua categoria é infantil.')
elif idade<19:
    print('Sua categoria é junior.')
elif idade<25:
    print('Sua categoria é sênior.')
else:
    print('Sua categoria é master.')
