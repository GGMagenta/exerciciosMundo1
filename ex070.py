# Pegue o nome e preço de varios produtos até quando não quiser mais continuar
# Mostre o preço total, quantos custam mais de R$1000, e o nome do mais barato
c=0
total = 0
caros = 0
maisBaratoNome = ''
maisBaratoPreco = 0
while True:
    nome = input('Digite o nome do produto: ').strip()
    preco = float(input('Digite o preço: R$'))
    if c == 0 or preco < maisBaratoPreco:
        maisBaratoNome = nome
        maisBaratoPreco = preco
    if preco >= 1000:
        caros += 1
    total += preco
    c += 1
    opcao = 'a'
    while opcao not in 'SsNn':
        opcao = input('Deseja continuar? [s/n]').strip()[0]
    if opcao in 'Nn':
        break
print(f'De {c} produtos cadastrados:')
print(f'O preço total é de R${total:.2f}.')
print(f'{caros} produtos custam mais de R$1000.')
print(f'O mais barato é {maisBaratoNome}, que custou R${maisBaratoPreco:.2f}.')
