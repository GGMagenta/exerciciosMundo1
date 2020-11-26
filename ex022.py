#Pegue um nome e mostre em letras maiusculas, minusculas, quantas letras sem espaço e quantas letras no primeiro nome
nome = input('Digite seu nome completo: ').strip()
# nome = nome.strip()
dividido = nome.split()
print(nome.upper())
print(nome.lower())
print(len(''.join(dividido)))
print(len(nome)-nome.count(' '))
print('o primeiro nome tem {} letras'.format(len(dividido[0])))
