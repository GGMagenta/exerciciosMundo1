# Pegue o peso a altura e calcule o IMC, depois classifique
# ate 18.5 abaixo do peso - ate 25 peso ideal - ate 30 sobrepeso - ate 40 obesidade - acima 40 obesidade morbida
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / altura ** 2
print('Seu IMC é de {:.1f}'.format(imc))
if imc<18.5:
    print('Você está abaixo do peso.')
elif imc<=25:
    print('Você es´ta no peso ideal, \033[1;33mparabêns!')
elif imc<=30:
    print('Você está com sobrepeso.')
elif imc<=40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')
