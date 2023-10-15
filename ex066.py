#LER VARIOS NUMEROS INTEIROS PELO USUARIO
#PARAR QUANDO DIGITAR 999
#MOSTRAR O TOTAL DE NÚMEROS
#MOSTRAR A SOMA ENTRE ELES
soma = cont = 0
while True:
    num = str(input('Informe um número inteiro ou 999 para sair: ')).strip()
    while num.isnumeric() == False:
        print('-=-' * 20)
        num = str(input('Valor digitado é inválido!\nInforme um número inteiro ou 999 para sair: ')).strip()
    num = int(num)
    if num != 999:
        soma += num
        cont += 1
    else:
        break
print('-=-' * 20)
print(f'Você digitou {cont:.0f} números e a soma destes números é {soma:.0f}.')
