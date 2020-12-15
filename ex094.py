# Pegue nome, sexo e idade de varias pessoas e guarde em um dicionario dentro de uma lista
# quantas pessoas cadastradas, média das idades, todas as mulheres, todos com idade acima da média
todos = []
media = 0
pessoa = {}
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = input('Sexo: [m/f] ').strip().lower()[0]
    pessoa['sexo'] = sexo
    media += pessoa['idade']
    todos.append(pessoa.copy())
    pessoa.clear()
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = input('Deseja continuar? [s/n] ').strip()[0]
    if opcao in 'Nn':
        break
print('=' * 50)
print(f'O total de pessoas cadastradas é {len(todos)}.')
media /= len(todos) # media =
print(f'A média das idades é {media:.2f}.')
mulheres = []
acimaMedia = []
for p in todos:
    if p['sexo'] == 'f':
        mulheres.append(p)
    if p['idade'] > media:
        acimaMedia.append(p)
if len(mulheres) > 0:
    print('=' * 50)
    print('Lista de todas as mulheres cadastradas:')
    for m in mulheres:
        print(f'{m["nome"]} com {m["idade"]} anos')
if len(acimaMedia) > 0:
    print('=' * 50)
    print('Lista de todas as pessoas com idade acima da média:')
    for a in acimaMedia:
        print(f'{a["nome"]} do sexo "{a["sexo"]}" com {a["idade"]} anos')
