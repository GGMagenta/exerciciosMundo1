# Pegue o ano de nascimento e diga se ainda vai se alistar, se ja pode se alistar, ou se ainda não se alistou no exercito
from datetime import date
# import datetime
ano = int(input('Informe o ano do seu nascimento: '))
anoAtual = date.today().year
idade = anoAtual-ano
# print(idade)
if idade<18:
    print('Você ainda irá se alistar dentro de {} anos.'.format(18-idade))
elif idade==18:
    print('Já está na hora se alistar.')
else:
    print('Você está {} anos atrasado para o alistamento.'.format(idade-18))

