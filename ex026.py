# Pegue uma frase e veja quantas letras "a" tem, e a posiçâo da primeira e última letras "a"
frase = input('Digite uma frase: ').strip().lower()
print('A frase tem {} letras "a", onde aparece primeiro na posicao {}, e por último {}'.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))
