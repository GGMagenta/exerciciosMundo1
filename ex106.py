#mini manual interativo usando o help do python
from time import sleep
def mensagem(msg, cor=0):
    tam = len(msg)+2
    print(cores[cor], end='')
    print('=' * tam)
    print(f' {msg}')
    print('=' * tam)
    print(cores[0], end='')
    sleep(1)


def ajuda(funcao):
    print(cores[3], end='')
    help(funcao)
    print(cores[0], end='')


#main
cores = ['\033[m', '\033[1;30;41m', '\033[1;30;44m', '\033[7m']
while True:
    mensagem('Sistema de ajuda',cor=1)
    f = input('Qual o nome da função que deseja procurar? (fim para sair) ').strip().lower()
    if f == 'fim':
        break
    else:
        mensagem(f'Acessando biblioteca {f}', cor=2)
        ajuda(f)
        sleep(1)
mensagem('Terminando programa.')
