# Pegue o nome do jogador de futebol e quantas partidas ele jogou
# quantidade de gols em cada partida e coloque em uma lista
# guarde tudo em um dicionário junto com o total de gols
jogador = {}
jogador['nome'] = input('Nome do jogador: ')
partidas = int(input('Quantas partidas jogou? '))
gols = []
totalGols = 0
for p in range(0, partidas):
    n = int(input(f'Quantos gols fez na {p + 1}a partida? '))
    totalGols += n
    gols.append(n)
# print(sum(gols))
jogador['partidas'] = gols[:]
jogador['gols'] = totalGols
print('=' * 50)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["partidas"])} partidas.')
for i, g in enumerate(jogador['partidas']):
    print(f'     => Na partida {i + 1} ele marcou {g} gols.')
print(f'O total foi de {jogador["gols"]} gols durante o campeonato.')