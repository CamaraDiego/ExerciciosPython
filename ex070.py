#LER NOME E PREÇO DE VARIOS PRODUTOS
#PERGUNTAR SE QUER CONTINUAR
#NO FINAL MOSTRAR:
#TOTAL GASTO NA COMPRA
#QUANTOS CUSTAM MAIS DE 1000
#NOME DO PRODUTO MAIS BARATO
from time import sleep
print('-=-' * 10)
print('CADASTRO DE PRODUTOS')
total = ptotal = mais = barato = nbarato = 0
while True:
    print('-=-' * 10)
    nome = str(input('Digite o nome do produto:\n')).strip()
    print('-=-' * 10)
    preco = str(input('Informe o preço do produto R$')).strip()
    print('-=-' * 10)
    while (preco.isnumeric() == False) and (preco.replace('.', '').isnumeric() == False):
        preco = str(input('Valor inválido, informe o preço do produto R$')).strip()
        print('-=-' * 10)
    sleep(0.5)
    preco = float(preco)
    total += 1
    ptotal += preco
    if preco > 1000:
        mais += 1
    if total == 1 or preco < barato:
        barato = preco
        nbarato = nome
    continua = str(input('Deseja continuar cadastrando produtos? [S/N]: ')).upper()
    while (continua in 'SN') == False:
        continua = str(input('Opção inválida, deseja continuar cadastrando produtos?\nDigite S para sim ou N para Não: ')).upper()
    if continua == 'N':
        break
print('-=-' * 15)
print('PROCESSANDO', end = '')
sleep(0.5)
print('.', end = '')
sleep(0.5)
print('.', end = '')
sleep(0.5)
print('.')
print('-=-' * 15)
sleep(0.5)
print(f'Foram cadastrados {total} produtos.')
sleep(0.5)
print(f'O total gasto na compra foi R${ptotal:.2f}.')
sleep(0.5)
print(f'{mais} produtos nesta compra custam mais de R$1000.00.')
sleep(0.5)
print(f'O produto mais barato foi {nbarato} custando R${barato:.2f}.')
