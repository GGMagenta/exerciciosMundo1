# Pegue o preço de um prduto e a forma de pagamento,e calcule o novo preço
# a vista 10% desconto - a vista no cartão 5% desconto - ate 2x preco normal - 3x ou mais 20% juros
preco = float(input('Qual o valor do produto? R$'))
pagamento = int(input("""Qual a forma de pagamento?
Digite 1 para pagar em dinheiro ou cheque.
Digite 2 para pagar com cartão a vista.
Digite 3 para pagar parcelado"""))
if pagamento == 1:
    print('O desconto de pagamento a vista é de 10%')
    preco = preco*0.9
    print('O preço final é de R${}'.format(preco))
elif pagamento == 2:
    print('O desconto de pagamento a vista no cartão é de 5%')
    preco = preco * 0.95
    print('O preço final é de R${}'.format(preco))
elif pagamento == 3:
    parcelas = int(input('Vai parcelar em quantas vezes? '))
    if parcelas<=2:
        print('Pagamento em até 2 vezes não tem desconto.')
        print('O preço final é de R${}'.format(preco))
    else:
        print('Pagamento em acima de 2 vezes recebem 20% de juros.')
        preco = preco*1.2
        print('O preço final é de R${}'.format(preco))
else:
    print('Não é uma forma valida de pagamento.')
