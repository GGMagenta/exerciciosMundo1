# Crie uma função ficha que recebe 2 param opcionais no nome e quantos gols marcou
# mostrar a ficha mesmo sem digitar nada
def ficha(nome='Não informado', gols='0'):
    """
    Gera uma ficha para o jogador
    :param nome: nome do jogador
    :param gols: quantos gols ele marcou
    :return: ficha do jogador
    """
    n = nome.strip()
    g = gols.strip()
    if len(n) == 0:
        n = 'Não informado'
    if not gols.isnumeric():
        g = '0'
    frase = 'O jogador '+n+' marcou '+g+' gol(s) no campeonato.'
    return frase


#main
nome = input('Nome do jogador: ')
gols = input('Quantos gols ele fez? ')
print(ficha(nome, gols))
#print(ficha())
