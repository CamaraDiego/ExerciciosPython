#LER IDADE, SEXO
#PERGUNTAR SE O USUARIO QUER CONTINUAR
#NO FINAL MOSTRAR
#QUANTAS TEM MAIS DE 18
#QUANTOS HOMENS CADASTRADOS
#QUANTAS MULHERES COM MENOS DE 20
from time import sleep
print('=== CADASTRAMENTO DE PESSOAS ===')
maiores = masculino = menos = total = 0
while True:
    print('-=-' * 15)
    idade = str(input('Informe a idade para cadastro: ')).strip()
    print('-=-' * 15)
    while (idade.isnumeric() == False) or (int(idade) < 0):
        idade = str(input('Valor inválido, informe a idade para cadastro: ')).strip()
        print('-=-' * 15)
    idade = int(idade)
    sleep(0.5)
    if idade >= 18:
        maiores += 1
    sexo = str(input('Informe o sexo para cadastro [M/F]: ')).upper()
    print('-=-' * 15)
    while (sexo in 'MF') == False:
        sexo = str(input('Dado inválido, informe o sexo para cadastro\ndigite M para masculino ou F para feminino: ')).upper()
        print('-=-' * 15)
    sleep(0.5)
    if sexo in 'M':
        masculino += 1
    elif sexo in 'F' and idade < 20:
        menos += 1
    total += 1
    continua = str(input('Quer continuar cadastrando mais pessoas? [S/N]: ')).upper()
    while (continua in 'SN') == False:
        continua = str(
            input('Dado inválido, quer continuar cadastrando mais pessoas?\nDigite S para sim ou N para não: ')).upper()
    sleep(0.5)
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
print(f'Nesta operação foram cadastradas ao todo {total} pessoas.')
print(f'Destas, {maiores} são maiores de idade.')
print(f'Foram cadastrados {masculino} pessoas do sexo masculino.')
print(f'E {menos} do sexo feminino com menos de 20 anos.')
