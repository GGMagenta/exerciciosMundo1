# pegue um número e mostre os termos da sequência de fibonacci
fim = int(input('Até qual termo deseja ver da Sequência de Fibonacci? '))
termo1 = 1
termo2 = 0
i = 0
while i < fim:
    if i > 1:
        soma = termo1 + termo2
        print(soma)
        termo2 = termo1
        termo1 = soma
    else:
        print(i)
    i += 1
