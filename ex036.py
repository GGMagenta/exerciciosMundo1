# Pegar valor da casa, o salario e em quantos anos vai pagar o emprestimo
# calcular o valor da prestação e negar se for acima de 30% do salario
casa = float(input('Qual o valor da casa que deseja comprar? R$ '))
salario = float(input('Qual o valor do seu salário? R$ '))
anos = int(input('Em quantos anos vai pagar o emprestimo? '))
prestacao = casa/(anos*12)
if prestacao >=salario*0.3:
    print('O emprestimo foi \033[1;31mNEGADO\033[m por exceder mais de 30% do valor do salário.')
else:
    print('O valor da prestação mensal será de \033[1;32mR$ {:.2f}'.format(prestacao))
