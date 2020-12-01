# Pegue um valor e informe quantas cédulas serão sacadas
# 50 , 20 , 10 , 1
nota = 50
cedulas = 0
valor = int(input('Qual o valor que deseja sacar? R$'))
while True:
    if valor >= nota:
        valor -= nota
        cedulas += 1
    else:
        if cedulas > 0:
            print(f'Total de {cedulas} cédulas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        if valor == 0:
            break
        cedulas = 0
print('+=' * 20, '\nOperação concluida.')
# while valor >= nota:
#     valor -= nota
#     cedulas += 1
