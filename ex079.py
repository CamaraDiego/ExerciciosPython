#USUÁRIO DIGITAR VÁRIOS VALORES NUMÉRICOS
#PERGUNTAR SE O USUÁRIO QUER CONTINUAR
#CADASTRAS OS VALORES EM UMA LISTA
#CASO A LISTA JÁ TENHA ESTE NÚMERO NÃO INSERIR E EXIBIR MENSAGEM DE FALHA
#NO FINAL EXIBIR OS VALORES EM ORDEM CRESCENTE
from time import sleep
lista = list()
print('-=-' * 15)
while True:
    valor = str(input('Digite um valor inteiro: ')).strip()
    while valor.isnumeric() == False:
        valor = str(input('Valor inválido, digite um valor inteiro: ')).strip()
    valor = int(valor)
    sleep(0.5)
    if lista.count(valor) != 0:
        print('Valor já inserido, portanto inválido.')
        print('-=-' * 15)
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso.')
        print('-=-' * 15)
    sleep(0.5)
    cont = str(input('Quer continuar? [S/N]: ')).upper()
    print('-=-' * 15)
    while (cont.isalpha() == False) or ((cont in 'SN') == False):
        cont = str(input('Quer continuar? [S/N]: ')).upper()
        print('-=-' * 15)
        sleep(0.5)
    if cont == 'N':
        break
sleep(1)
print('Os valores inseridos na lista, em ordem crescente são:')
sleep(1)
print(sorted(lista))
print('-=-' * 15)
