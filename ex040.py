#LER DUAS NOTAS DE UM ALUNO
#ABAIXO DE 5 REPROVADO
#ENTRE 5 E 6.9 RECUPEERACAO
#MAIOR OU IGUAL A 7 APROVADO

n1 = str(input('Informe a primeira nota: ')).strip()
n1 = float(n1)
n2 = str(input('Informe a segunda nota: ')).strip()
n2 = float(n2)
media = (n1 + n2) / 2
vermelho = '\033[1:31m'
amarelo = '\033[1:33m'
verde = '\033[1:32m'
cancel = '\033[m'
if media < 5:
    print('Sua média é de {:.2f} portanto está {}reprovado{}.'.format(media, vermelho, cancel))
elif 5 <= media <= 6.9:
    print('Sua média é de {:.2f} portanto está em {}recuperação{}.'.format(media, amarelo, cancel))
else:
    print('Sua média é de {:.2f}, PARABÉNS, você está {}aprovado{}!'.format(media, verde, cancel))
