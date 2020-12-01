# Pegue idade e sexo de varias pessoas, só pare quando não quiser mais continuar
# Informar quantas tem mais de 18, quantos homens, e quantas mulheres com menos de 20 anos
total = 0
homens = 0
maior = 0
jovensF = 0
while True:
    sexo = 'a'
    while sexo not in 'MmFf':
        sexo = input('Masculino ou Feminino? [m/f] ').strip()[0]
    idade = int(input('Qual a idade?' ))
    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        homens += 1
    elif idade < 20:
        jovensF += 1
    total +=1
    opcao = 'a'
    while opcao not in 'SsNn':
        opcao = input('Deseja continuar? [s/n]').strip()[0]
    if opcao in 'Nn':
        break
print(f'No total de {total} pessoas cadastradas:\n{maior} tem mais de 18 anos.\n{homens} são homens.\n{jovensF} são mulheres com menos de 20 anos.')