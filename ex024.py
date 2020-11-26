# Pegue um nome e veja se começa com "Santo"
nome = input('Digite o nome de uma cidade ').strip()
dividido = nome.split()
print(nome[:5].upper() == 'SANTO')
print('A cidade começa com Santo? {}'.format('santo' in dividido[0].lower()))
