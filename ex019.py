# Pegue o nome de 4 alunos e sorteie um nome
import random
lista = []
lista.append(input('nome do aluno 1: '))
lista.append(input('nome do aluno 2: '))
lista.append(input('nome do aluno 3: '))
lista.append(input('nome do aluno 4: '))
n = random.randint(0, 3)
print('o sorteado foi o aluno {}, que se chama {}'.format(n+1,lista[n]))
# print('o sorteado foi {}'.format(random.choice(lista)))
