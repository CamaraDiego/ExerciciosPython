#SIMULAR O FUNCIONAMENTO DE UM CAIXA ELETRONICO
#PERGUNTAR O VALOR A SER SACADO
#INFORMAR QUANTAS CEDULAS DE CADA VALOR SERÃO ENTREGUE
#TRABALHA APENAS COM NOTAS DE 50 20 10 E 1
from time import sleep
print('-=-' * 8)
print('=== CAIXA ELETRÔNICO ===')
print('-=-' * 8)
valor = str(input('Insira o valor para saque R$')).strip()
print('-=-' * 8)
while (valor.isnumeric() == False):
    valor = str(input('==== VALOR INVÁLIDO ====\nInsira o valor para saque R$')).strip()
    print('-=-' * 8)
valor = float(valor)
n50 = valor // 50
n20 = (valor - (n50 * 50)) // 20
n10 = (valor - (n50 * 50) - (n20 * 20)) // 10
n01 = (valor - (n50 * 50) - (n20 * 20) - (n10 * 10)) // 1
print('PROCESSANDO', end = '')
sleep(0.5)
print('.', end = '')
sleep(0.5)
print('.', end = '')
sleep(0.5)
print('.')
print('-=-' * 8)
print(f'Para o saque de R${valor:.2f} será entregue:')
sleep(0.5)
if n50 > 0:
    print(f'{n50:.0f} notas de R$50')
if n20 > 0:
    print(f'{n20:.0f} notas de R$20')
if n10 > 0:
    print(f'{n10:.0f} notas de R$10')
if n01 > 0:
    print(f'{n01:.0f} notas de R$1')
if n50 == n20 == n10 == n01 == 0:
    print('Nenhum valor selecionado.')
