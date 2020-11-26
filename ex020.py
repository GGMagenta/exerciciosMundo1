#Pegue o nome de 4 alunos e sorteie a ordem
import random
lista = []
lista.append(input('nome do aluno 1: '))
lista.append(input('nome do aluno 2: '))
lista.append(input('nome do aluno 3: '))
lista.append(input('nome do aluno 4: '))
random.shuffle(lista)
# n1=lista.pop(random.randint(0,len(lista)-1))
# n2=lista.pop(random.randint(0,len(lista)-1))
# n3=lista.pop(random.randint(0,len(lista)-1))
# n4=lista.pop(random.randint(0,len(lista)-1))
# print('a ordem ficou {0}, depois {1},depois {2}, e por ultimo {3}'.format(n1,n2,n3,n4))
print('a ordem sera:\n{}'.format(lista))
