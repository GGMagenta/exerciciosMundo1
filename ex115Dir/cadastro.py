def cadastrar():
    """
    Pega as informações de nome e idade e coloca em um arquivo de texto
    :return: nada
    """
    from ex115Dir import arquivo
    nome = inputNome('Qual o nome? ')
    idade = inputIdade('Qual a idade? ')
    arquivo.adicionar(nome, idade)
    print(f'Cadastro de {nome} adicionado.\n')


def inputNome(msg):
    while True:
        n = input(msg).strip()
        if len(n) > 0:
            break
        else:
            print('\033[1;31mNome Inválido.\033[m')
    return n


def inputIdade(msg):
    """
        Pega um número e valida se é uma idade
        :param msg: mensagem a ser dita para pegar o valor
        :return: idade validada
        """
    while True:
        valor = input(msg).strip()
        try:
            numero = int(valor)
            break
        except KeyboardInterrupt:
            print('Não foi informado uma idade.')
            return 0
        except:
            print('\033[1;31mERRO! Digite uma idade válida.\033[m')
    return numero

