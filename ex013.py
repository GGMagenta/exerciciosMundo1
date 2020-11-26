#Pegue o salario e calcule com o aumento
salario = float(input('salario: '))
aumento = float(input('aumento: '))
print('O novo salario com aumento de {}% e de {:.2f}'.format(aumento,salario*(1+aumento/100)))
print(salario + (salario * aumento / 100), salario * aumento / 100)
