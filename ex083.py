# Pegue uma expressão matematica e veja se é valida com os parênteses corretos
calculo = input('Digite a expressão matematica: ').strip().lower()
parenteses = 0
#cada "(" adiciona 1 , cada ")" subtrai 1, se ficar negativo ou terminar >0 da erro
for pa in calculo:
    if pa == '(':
        parenteses += 1
    elif pa == ')':
        parenteses -= 1
    if parenteses < 0:
        break
if parenteses == 0:
    print('A expressão é valida')
else:
    print('A expressão é invalida')