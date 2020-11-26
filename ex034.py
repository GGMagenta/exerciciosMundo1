# Calcular o aumento de 10% do salário do funcionario, se for menor ou igual que R$1250, o aumento é de 15%
salario = float(input('Digíte o valor do salário: '))
if salario>1250:
    print('Salario acima de R$1250 recebem o aumento de 10%')
    aumento = 1.10
else:
    print('Salario abaixo de R$1250 recebem o aumento de 15%')
    aumento = 1.15
print('O novo salário é de R${:.2f}'.format(salario * aumento))
