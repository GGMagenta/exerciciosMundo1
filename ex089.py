# ler nome e 2 notas do aluno e guarde na lista composta
# calcule a média de cada um e as notas individualmente
boletim = [[], []]  #0 aluno - 1 notas
while True:
    aluno = []
    notas = []
    nome = input('Nome: ')
    aluno.append(nome)
    nota1 = float(input('Nota1: '))
    notas.append(nota1)
    nota2 = float(input('Nota2: '))
    notas.append(nota2)
    media = (nota1 + nota2) / 2
    aluno.append(media)
    boletim[0].append(aluno[:])
    boletim[1].append(notas[:])
    aluno.clear()
    notas.clear()
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = input('Deseja continuar? [s/n] ').strip()[0]
    if opcao in 'Nn':
        break
print('-='*20)
print(f'{"n°":<3}{"nome":<10}{"média"}')
print('-' * 18)
for i, a in enumerate(boletim[0]):
    print(f'{i:<3}{a[0]:<10}{a[1]:.1f}')
n = 0
while True:
    n = int(input('Deseja ver as notas de qual aluno? [999 para sair] '))
    if n == 999:
        break
    elif n < len(boletim[0]):
        print(f'As notas de {boletim[0][n][0]} são: {boletim[1][n]}')
print('Programa encerrado.')

