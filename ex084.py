# Pegue nome e peso das pessoas e coloque na lista
# mopstre o total, lista com amis pesados e lista com mais leves
lista = []
dados = []
maior = 0
menor = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    if len(lista) == 1:
        maior = menor =dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    dados.clear()
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = input('Deseja continuar? [s/n] ').strip()[0]
    if opcao in 'Nn':
        break
print(f'Tem {len(lista)} pessoas cadastradas.')
maisPesados = []
menosPesados = []
for p in lista:
    if p[1] == maior:
        maisPesados.append(p[0])
    elif p[1] == menor:
        menosPesados.append(p[0])
print(f'Os mais pesados são: {maisPesados} com {maior:.2f}Kg')
print(f'Os menos pesados são: {menosPesados} com {menor:.2f}Kg')
