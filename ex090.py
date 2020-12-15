# Pegue o nome e média de um aluno, veja a situação e coloque tudo no dicionário
aluno = {}
aluno['nome'] = input('Nome do aluno(a): ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] > 5:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print(f'O aluno {aluno["nome"]}, teve uma média de {aluno["media"]:.1f} e foi {aluno["situacao"]}.')
