# Pegue 2 notas, calcule a média e diga se foi aprovado
# até 5.0 - reprovado    5.1 a 6.9 - recuperação   7.0 - aprovado
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
print('Sua média foi {:.1f}'.format(media))
# 7 < media <= 5
if media > 7:
    print('Você foi \033[1;32mAPROVADO!')
elif media >= 5:
    print('Você está de recuperação.')
else:
    print('Voce foi \033[1;31mREPROVADO!')
