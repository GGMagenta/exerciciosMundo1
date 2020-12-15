# Refaça a função leiaInt() incluindo digitação de número invalido
# Crie também a leiaFloat()
def leiaint(mensagem):
    """
    similar a função input, mas recebe apenas um valor inteiro
    :param mensagem: mensagem a ser dita para pegar o valor
    :return: número inteiro
    """
    while True:
        valor = input(mensagem).strip()
        try:
            numero = int(valor)
            break
        except KeyboardInterrupt:
            print('Não foi informado um número.')
            return 0
        except:
            print('\033[1;31mERRO! Digite um valor inteiro válido.\033[m')
    return numero


def leiafloat(mensagem):
    """
    similar a função input, mas recebe apenas um valor real
    :param mensagem: mensagem a ser dita para pegar o valor
    :return: número real
    """
    while True:
        valor = input(mensagem).strip().replace(',', '.')
        try:
            numero = float(valor)
            break
        except KeyboardInterrupt:
            print('Não foi informado um número.')
            return 0
        except:
            print('\033[1;31mERRO! Digite um valor real válido.\033[m')
    return numero


#main
i = leiaint('Digite um número Inteiro: ')
r = leiafloat('Digite um número Real: ')
print(f'O valor inteiro é {i}, e o valor real é {r}.')