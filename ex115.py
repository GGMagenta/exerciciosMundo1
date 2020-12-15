# Crie um sistema modularizado de cadastrar pessoas com nome e idade em um arquivo de texto
# Tem apenas as opçoes de cadastrar e ler todos cadastrados
from ex115Dir import arquivo
from ex115Dir import cadastro
def titulo(msg):
    tamanho = len(msg) + 4
    print('-' * tamanho)
    print(f'  {msg}')
    print('-' * tamanho)


#main
while True:
    titulo('Sistema de cadastro')
    print('1-Ver pessoas cadastradas.')
    print('2-Adicionar pessoa no cadastro.')
    print('3-Sair do sistema.')
    opcao=0
    while True:
        try:
            opcao = int(input('Qual a sua ação? ').strip())
            if 0 < opcao < 4:
                break
            else:
                print('Por favor escolha uma opção válida.')
        except:
            print('\033[1;31mERRO! Por favor digite um número inteiro.\033[m')
    if opcao == 1:
        titulo('Lista de pessoas cadastradas')
        print(f'\033[7m{arquivo.mostrarLista()}\033[m')
    elif opcao == 2:
        titulo('Lista de pessoas cadastradas')
        print('\n')
        cadastro.cadastrar()
    elif opcao == 3:
        titulo('Saindo do programa')
        break
print('Programa encerrado.')