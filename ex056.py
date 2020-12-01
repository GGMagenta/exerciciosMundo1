# Pegue nome, sexo e idade de 4 pessoas e mostre:
# media das idades
# nome do homem mais velho
# quantas mulheres com menos de 20
idades = 0
maisVelhoNome = ''
maisVelhoIdade = 0
mulheresJovens = -1
for i in range(0, 4):
    nome = input('Digite o nome: ').strip()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite "M" para Masculino e "F" para Feminino: ').strip().upper()
    # sexo in 'Mm'
    if sexo == 'M':
        if maisVelhoIdade == 0:
            maisVelhoIdade = idade
            maisVelhoNome = nome
        elif maisVelhoIdade<idade:
            maisVelhoIdade = idade
            maisVelhoNome = nome
    else:
        if mulheresJovens == -1:
            mulheresJovens = 0
        if idade < 20:
            mulheresJovens += 1
    idades += idade
media = idades/4
print('\n', '='*30, '\n')
print('A media das idades registradas é {:.1f}'.format(media))
if maisVelhoIdade > 0:
    print('O homem mais velho se chama {} e tem {} anos.'.format(maisVelhoNome,maisVelhoIdade))
else:
    print('Não tem nenhum homem na lista.')
if mulheresJovens > -1:
    print('No registro tem {} mulhermes com menos de 20 anos.'.format(mulheresJovens))
else:
    print('Não tem nenhuma mulher na lista.')
