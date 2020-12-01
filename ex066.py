# Pegue varios números até digitar 999, depois mostre quantos números e a soma deles
c = soma = 0
while True:
    n = int(input('Digite um número, e "999" para parar: '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'Você digitou {c} números, e a soma de todos eles é {soma}')