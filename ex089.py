#LER NOME E DUAS NOTAS DE VARIOS ALUNOS E GUARDAR EM UMA LISTA COMPOSTA (PERGUNTAR SE QUER CONTINUAR)
#PRIMEIRO ELEMENTO É O NOME E SEGUNDO ELEMENTOS CONTENDO AS DUAS NOTAS
#NO FINAL MOSTRAR UM BOLETIM COM A MEDIA DE CADA UM E PERMITIR QUE O USUARIO MOSTRE AS NOTAS DE CADA UM INDIVIDUALMENTE
#PARA CONTINUAR DIGITAR O CODIGO DO ALUNO OU ZERO PARA PARAR
ficha = list()
while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome], [nota1, nota2], [media])
    resp = str(input('Quer continuar? [S/N]: ')).upper()
    if resp in 'N':
        break
print('-=-' * 15)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-=-' * 15)
for i, a in enumerate(ficha):
    print(f'{i:<4}{ a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=-' * 15)
    opc = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}.')
print('VOLTE SEMPRE')
