# Pegue o primeiro termo de uma PA e a razão e mostre até o 10 termo usando while
# Pergunte se quer mostrar mais números até digitar 0
primeiro = float(input('Digite o primeiro termo da PA: '))
razao = float(input('Digite a razão:'))
termo = 0
maisTermos = 1
ultimoTermo = 10
while termo < 10:
    print('{} - '.format(termo+1), primeiro + razao * termo)
    termo += 1
while maisTermos > 0:
   maisTermos = int(input('Mais quantos termos deseja mostrar? '))
   ultimoTermo += maisTermos
   while termo < ultimoTermo:
       print('{} - '.format(termo + 1), primeiro + razao * termo)
       termo += 1
print('Terminou')
