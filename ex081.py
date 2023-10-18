#LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA, PERGUNTAR SE QUER CONTINUAR
#MOSTRAR
#QUANTOS NÚMEROS FORAM DIGITADOS
#A LISTA EM FORMA DECRESCENTE
#SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA E QUAL SUA POSIÇÃO CASO HAJA
from time import sleep
lista = list()
while True:
    valor = str(input('Digite um valor inteiro: ')).strip()
    while valor.isnumeric() == False:
        valor = str(input('Valor inválido, digite um valor inteiro: ')).strip()
    valor = int(valor)
    lista.append(valor)
    cont = str(input('Quer continuar? [S/N]: ')).upper()
    while (cont.isalpha() == False) or ((cont in 'SN') == False):
        cont = str(input('Dado inválido, quer continuar? [S/N]: ')).upper()
    if cont == 'N':
        break
print('-=-' * 15)
sleep(1)
print(lista)
sleep(1)
print(f'Nesta lista foram digitados {len(lista)} números.')
sleep(1)
if lista.count(5) != 0:
    print(f'A primeira ocorrência do número 5 é na posição {lista.index(5) +1}.')
else:
    print('O número 5 não foi digitado nenhuma vez.')
sleep(1)
print('-=-' * 15)
sleep(1)
print(f'Em ordem decrescente são:')
sleep(1)
lista.sort(reverse = True)
print(lista)
