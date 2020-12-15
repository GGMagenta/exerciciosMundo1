# refazer o 93 com varios jogadores e selecionar o jogador que quiser ver
jogadores = []
jogador = {}
while True:
    jogador['nome'] = input('Nome do jogador: ')
    partidas = int(input('Quantas partidas jogou? '))
    gols = []
    totalGols = 0
    for p in range(0, partidas):
        n = int(input(f'Quantos gols fez na {p + 1}a partida? '))
        totalGols += n
        gols.append(n)
    jogador['partidas'] = gols[:]
    jogador['gols'] = totalGols
    jogadores.append(jogador.copy())
    jogador.clear()
    opcao = ' '
    while opcao not in 'SsNn':
        opcao = input('Deseja continuar? [s/n] ').strip()[0]
    if opcao in 'Nn':
        break
print('=' * 50)
print(f'{"n°":<3}{"Jogador":<15}{"total":<8}{"gols"}')
for i, j in enumerate(jogadores):
    print(f'{i:<3}{j["nome"]:<15}{j["gols"]:<8}{j["partidas"]}')
    # for v in j.values(): print(f'{v:<15}')
while True:
    opcao = -1
    while True:
        opcao = int(input('Qual o n° do jogador que deseja ver os dados? (999 para sair)'))
        if opcao == 999 or 0 <= opcao < len(jogadores):
            break
        else :
            print('Valor invalido!')
    if opcao == 999:
        print('Programa finalizado.')
        break
    print(f'O jogador {jogadores[opcao]["nome"]} jogou {len(jogadores[opcao]["partidas"])} partidas.')
    for i, g in enumerate(jogadores[opcao]['partidas']):
        print(f'     => Na partida {i + 1} ele marcou {g} gols.')
    print(f'O total foi de {jogadores[opcao]["gols"]} gols durante o campeonato.')