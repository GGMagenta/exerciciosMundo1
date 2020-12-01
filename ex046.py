# Contagem regressiva de 10 ate 0 com pausa e 1 segundo
from time import sleep
print('Contagem regressiva para os fogos de artifício')
sleep(3)
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('BOOM\nOlhe os fogos!')