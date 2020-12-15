def adicionar(nome, idade):
    """
    Coloca no arquivo o nome e a idade
    :param nome: nome a ser cadastrado
    :param idade: idade a ser cadastrada
    :return:nada
    """
    arquivo = open('Cadastros.txt', 'a+')
    arquivo.write(f'NOME : {nome:<29} IDADE: {idade}\n')
    arquivo.close()


def limpar():
    """
    Limpa todos os cadastros
    :return: nada
    """
    arquivo = open('Cadastros.txt', 'w+')
    arquivo.write('')
    arquivo.close()


def mostrarLista():
    """
    Pega todas as pessoas cadastradas e mostra na tela
    :return: lista de todas as pessoas cadastradas
    """
    try:
        arquivo = open('Cadastros.txt', 'r')
        return arquivo.read()
    except:
        return 'O arquivo não existe.'
