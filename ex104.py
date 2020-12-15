# Criar função leiaint que só vai aceitar um valor númerico
def leiaint(mensagem):
    """
    similar a função input, mas recebe apenas um valor inteiro
    :param mensagem: mensagem a ser dita para pegar o valor
    :return: número inteiro
    """
    while True:
        valor = input(mensagem).strip()
        if not valor.isnumeric():
            print('Valor Invalido!')
        else:
            break
    return int(valor)


# main
n = leiaint('Digite um valor inteiro: ')
print(f'O valor digitado foi {n}.')
