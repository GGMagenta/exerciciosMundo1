# Pegue o sexo ( M ou F ) e se estiver errado pegue novamente até que esteja certo
sexo = input('Digite o sexo [M/F]: ').upper().strip()
while sexo not in 'MF' or len(sexo) != 1:
    sexo = input('Valor inválido, tente novamente [M/F]: ').upper().strip()
print('Você digitou \033[1;31m{}'.format(sexo))
# sexo = input('Digite o sexo [M/F]: ').upper().strip()[0]
# while sexo not in 'MF':
