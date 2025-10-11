lista_alunos = []
nome1 = input('Nome 1:')
nome2 = input('Nome 2:')
nome3 = input('Nome 3:')

lista_alunos.append(nome1)
lista_alunos.append(nome2)
lista_alunos.append(nome3)

notas_alunos1 = [float(input(f'nota 1:{nome1}')), float(input(f'nota 2 :{nome1}'))]
notas_alunos2 = [float(input(f'nota 1:{nome2}')), float(input(f'nota 2 :{nome2}'))]
notas_alunos3 = [float(input(f'nota 1:{nome3}')), float(input(f'nota 2 :{nome3}'))]

media_aluno1 = sum(notas_alunos1)/len(notas_alunos1)
media_aluno2 = sum(notas_alunos2)/len(notas_alunos2)
media_aluno3 = sum(notas_alunos3)/len(notas_alunos3)

print('Media Alunos')
print(f'''
Medias:
aluno{nome1} - {media_aluno1}
aluno{nome2} - {media_aluno2}
aluno{nome3} - {media_aluno3}

''')

aprovado_1 = media_aluno1 >= 7
aprovado_2 = media_aluno2 >= 7
aprovado_3 = media_aluno3 >= 7 

print(f'''
{nome1} - APROVADO - {aprovado_1}
{nome2} - APROVADO - {aprovado_2}
{nome3} - APROVADO - {aprovado_3}

''')