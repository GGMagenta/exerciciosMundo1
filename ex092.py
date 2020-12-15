# Pegue nome, ano de nascimento ( mas cadasstrar idade),
# carteira de trabalho e guarde no dicionário
# se CTPS != 0 pegue ano de contratação e salário e mostre com quantos anos vai se aposentar (35 anos)
from datetime import date
# from datetime import datetime
anoAtual = date.today().year  # datetime.now().year
cadastro = {}
cadastro['nome'] = input('Nome: ')
anoNasc = int(input('Ano de nascimento: '))
cadastro['idade'] = anoAtual - anoNasc
cadastro['ctps'] = int(input('Carteira de trabalho (0 caso não tenha): '))
if cadastro['ctps'] > 0:
    cadastro['contratacao'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: R$'))
    anosTrabalho = anoAtual - cadastro['contratacao']
    cadastro['aposentadoria'] = 35 - anosTrabalho + cadastro['idade']
print('=' * 50)
for k, v in cadastro.items():
    print(f'{k} = {v}')
