#FUNÇÃO CHAMADA NOTAS
#INSERIR NOTAS DE UMA TURMA
#INFORMAR QUANTAS NOTAS FORAM PASSADAS
#QUAL O VALOR DA MAIOR
#QUAL O VALOR DA MENOR
#A MÉDIA DAS NOTAS
#E DE FORMA OPCIONAL A SITUAÇÃO DA MEDIA (SIT=FALSE)

def notas(notas, sit = False):
    from time import sleep
    pasta = dict()
    print('-=-' * 15)
    sleep(0.5)
    print(f'Foram informadas {len(notas)} notas.')
    pasta['total'] = len(notas)
    sleep(0.5)
    print(f'A maior nota foi {max(notas)}.')
    pasta['maior'] = max(notas)
    sleep(0.5)
    print(f'A menor nota foi {min(notas)}.')
    pasta['menor'] = min(notas)
    sleep(0.5)
    soma = 0
    for c in notas:
        soma += c
    media = soma / len(notas)
    print(f'A média das notas é {media:.2f}.')
    pasta['média'] = media
    if sit == True:
        if media < 5:
            print('Reprovação')
            pasta['situação'] = 'Reprovação'
        if 5 <= media < 7:
            print('Recuperação')
            pasta['situação'] = 'Recuperação'
        if 7 <= media:
            print('Aprovação')
            pasta['situação'] = 'Aprovação'
    sleep(0.5)
    print('-=-' * 15)
    return pasta

lista = list()
while True:
    lista.append(float(input('Digite a nota: ')))
    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if cont == 'N':
        break


dicionario = notas(lista, True)
print(dicionario)
