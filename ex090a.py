#PERGUNTAR NOME E MÉDIA DE UM ALUNO
#GUARDAR ALÉM DISSO A SITUAÇÃO
#NO FINAL EXIBIR O NOME A MEDIA E A SITUAÇÃO

nome = str(input('Informe o nome: ')).strip()
media = float(input('Informe a média: '))
situacao = ''
if media < 5:
    situacao = 'Reprovado'
elif 5 <= media < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Aprovado'
dicionario = {'nome' : nome, 'media' : media, 'situacao' : situacao}
print(f'Aluno {dicionario["nome"]}')
print(f'Média igual a {dicionario["media"]}')
print(f'Sua situação é {dicionario["situacao"]}')
