#LER NOME E PESO DE PESSOAS, PERGUNTAR SE QUER PARAR
#COLOCAR OS VALORES EM UMA LISTA
#MOSTRAR
#QUANTAS PESSOAS FORAM CADASTRADAS
#LISTAGEM COM AS 2 PESSOAS MAIS PESADAS (OU 1)
#LISTAGEM COM AS 2 PESSOAS MAIS LEVES (OU 1)
lista = list()
temp = list()
maior = menor = 0
while True:
    nome = str(input('Informe o nome: '))
    while nome.isalpha() == False:
        nome = str(input('Dado inválido, informe o nome: '))
    temp.append(nome)
    peso = str(input('Informe o peso: ')).strip()
    while (peso.isnumeric() == False) and (peso.replace('.', '').isnumeric() == False):
        peso = str(input('Dado inválido, informe o peso: ')).strip()
    peso = int(peso)
    temp.append(peso)
    if len(lista) == 0:
        menor = temp[1]
        maior = temp[1]
    elif len(lista) != 0:
        if temp[1] < menor:
            menor = temp[1]
        if temp[1] > maior:
            maior = temp[1]
    lista.append(temp[:])
    temp.clear()
    continuar = str(input('Deseja continuar? [S/N]: ')).upper()
    while (continuar.isalpha() == False) or ((continuar in 'SN') == False):
        continuar = str(input('Dado inválido, deseja continuar? [S/N]: ')).upper()
    if continuar == 'N':
        break
print('-=-' * 20)
print(f'O menor peso registrado foi {menor}Kg. As pessoas com este peso são:')
for pos in lista:
    if pos[1] == menor:
        print(f'[{pos[0]}]', end = ' ')
print('\n')
print('-=-' * 20)
print(f'O maior peso registrado foi {maior}Kg. As pessoas com este peso são:')
for pos in lista:
    if pos[1] == maior:
        print(f'[{pos[0]}]', end = ' ')
