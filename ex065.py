#LER VARIOS NUMEROS
#PERGUNTAR SE QUER CONTINUAR
#MOSTRAR A MEDIA ENTRE TODOS
#QUAL FOI O MAIOR E O MENOR
soma = maior = menor = cont = 0
print('-=-' * 15)
segue = ''
while segue != 'N':
    num = str(input('Informe um número: '))
    while (num.isnumeric() == False) and (num.replace('.', '').isnumeric() == False):
        num = str(input('Valor inválido, informe um número: '))
    num = float(num)
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num < menor:
            menor = num
        elif num > maior:
            maior = num
    segue = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while (segue.isalpha() == False) or ((segue in 'SN') == False):
        segue = str(input('Quer continuar? [S/N]: ')).strip().upper()
    print('-=-' * 15)
print('A média dos valores digitados é {:.2f}.'.format(soma / cont))
print('O maior valor digitado foi {:.2f}.'.format(maior))
print('O menor valor digitados foi {:.2f}.'.format(menor))
