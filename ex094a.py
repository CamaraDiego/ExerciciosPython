#LER NOME SEXO E IDADE
#GUARDAR EM UM DICIONÁRIO E TODOS EM UMA LISTA
#MOSTRAR QUANTAS PESSOAS FORAM CADASTRADAS
#A MEDIA DE IDADE DO GRUPO
#UMA LISTA COM TODAS AS MULHERES
#UMA LISTA COM PESSOAS COM IDADE ACIMA DA MÉDIA
from time import sleep
dicionario = dict()
lista = list()
qnt = somaidade = 0
while True:
    dicionario['nome'] = str(input('Informe o nome: ')).strip()
    dicionario['sexo'] = str(input('Informe o sexo [M/F]: ')).strip().upper()
    dicionario['idade'] = float(input('Informe a idade: '))
    lista.append(dicionario.copy())
    qnt += 1
    somaidade += dicionario['idade']
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print('-=-' * 20)
sleep(0.5)
print(f'A) Ao todo temos {qnt} pessoas cadastradas.')
sleep(0.5)
mediaidade = somaidade / qnt
print(f'B) A média de idade é de {mediaidade:.2f} anos.')
sleep(0.5)
print(f'C) As mulheres cadastradas foram: ')
sleep(0.5)
for valor in lista:
    if valor['sexo'] == 'F':
        print(f'{valor["nome"]}', end = ' ')
        sleep(0.5)
print()
print('D) A lista de pessoas acima da média:')
sleep(0.5)
for valor in lista:
    if valor['idade'] > mediaidade:
        for k, v in valor.items():
            print(f'{k} = {v}', end = ' ')
            sleep(0.5)
        print()
print('<<ENCERRADO>>')
print('-=-' * 20)
