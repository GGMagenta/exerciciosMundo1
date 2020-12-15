# Crie uma tubla com os 20 primeiros colocados do campeonato de futebol
# mostre os 5 primeiros, os 4 últimos, em ordem alfabetica e qual a posicao da Chapecoense
# NOTA, retirada lista do fim de 2020, não têm Chapecoence então usei Bahia
times = ('Atlético-MG', 'São Paulo', 'Flamengo', 'Internacional', 'Palmeiras',
         'Santos', 'Grêmio', 'Fluminence', 'Fortaleza', 'Ceará SC',
         'Corinthians', 'Athletico-PR', 'Bahia', 'Atlético-GO', 'Bragantino',
         'Sport Recife', 'Vasco da Gama', 'Coritiba', 'Botafogo', 'Goiás')
print('A ordem dos 5 Primeiros colocados:') # times[:5]
for i in range(0, 5):
    print(f'{i + 1}° - {times[i]}')
print('+-' * 20)
print('A ordem dos 4 Últimos colocados:') # times[16:] ou times[-4:]
for i in range(16, 20):
    print(f'{i + 1}° - {times[i]}')
print('+-' * 20)
print('A ordem dos times em ordem alfabética:')
ordem = sorted(times)
for time in ordem:
    print(time)
print('+-' * 20)
bahiaPos = times.index('Bahia') + 1
print(f'O time da Bahia está em {bahiaPos}°')