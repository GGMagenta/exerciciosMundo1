def leiaDinheiro(msg):
    """
    Pede um valor no teclado e valida se é um valor monetário.
    Só para quando recebe um valor válido.
    :param msg: Mensagem que mostra na tela
    :return: Valor monetário validado.
    """
    while True:
        v = input(msg).strip()
        if len(v) == 0:
            print('Não foi digitado nenhum valor!')
        else:
            v= v.replace(',', '.')
            charinvalido = False
            for c in v:
                if c not in '0123456789.':
                    charinvalido = True
                    break
            if not charinvalido:
                numero = float(v)
                break
            else:
                print(f'"{v}" não é um valor válido.')
    return numero
