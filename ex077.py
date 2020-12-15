# Crie um tupla com várias palavras e mostre as vogais de cada uma delas
tupla= ('Abacaxi', 'Pera', 'Pessego', 'Uva', 'Jabuticaba', 'Melancia', 'Amora')
for fruta in tupla:
    print(f'As vogais da palavra {fruta.lower()} são: ', end='')
    for letra in fruta.lower():
        if letra in 'aeiou':  # letra in 'aáâàãeéèê...etc'
            print(f'{letra} ', end='')
    print('')
print('Terminou.')