# Gere 4 jogadores que jogaram um dado, coloque em ordem no dicionario e mostre o vencedor
from random import randint
from time import sleep

jogadores = {'Jogador1': randint(1, 6),
             'Jogador2': randint(1, 6),
             'Jogador3': randint(1, 6),
             'Jogador4': randint(1, 6)
             }
print('Iniciando Jogo...')
sleep(1.5)
numeros = []
for k, v in jogadores.items():
    print(f'{k} rolou o número {v}.')
    numeros.append(v)
    sleep(1)
numeros.sort(reverse=True)  # valores ordem decrescente
ordem = []
for n in numeros:  # vasculhar valores do maior ao menor para cada item do dicionário
    for k, v in jogadores.items():
        if n == v and k not in ordem:
            ordem.append(k)
            ordem.append(n)
# print(ordem)
print('Finalizando Jogo...')
sleep(1.5)
for i in range(0, 4):
    print(f'Em {i + 1}° ficou {ordem[i * 2]} que rolou {ordem[i * 2 + 1]}')
    sleep(1)

# from operator import itemgetter
# ordenado = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
# print(ordenado) retorna lista com tuplas
