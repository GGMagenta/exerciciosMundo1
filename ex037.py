# Pegue um numero e pergunte para qual base deseja converter
# 1 - Binário  2 - Octal  3 - Hexadecimal
n = int(input('Digite o número que deseja converter: '))
opcao = int(input('Digite \033[31m1\033[m para converter para \033[31mbinário\033[m, \033[32m2\033[m'
                  'para \033[32moctal\033[m, e \033[33m3\033[m para \033[33mhexadecimal\033[m: '))
if opcao == 1:
    print('O número \033[31m{}\033[m em binário é {}'.format(n, '{0:b}'.format(n)))
    # print('O número \033[31m{}\033[m em binário é {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('O número \033[32m{}\033[m em octal é {}'.format(n, '{0:o}'.format(n)))
    # print('O número \033[32m{}\033[m em octal é {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('O número \033[33m{}\033[m em hexadecimal é {}'.format(n, '{0:x}'.format(n).upper()))
    # print('O número \033[33m{}\033[m em hexadecimal é {}'.format(n, hex(n)[2:].upper()))
else:
    print('{} não é uma opção valida.'.format(opcao))
