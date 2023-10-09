#LER UM NUMERO DE 0 A 9999
#EXIBIR OS DIGITOS SEPARADOS POR
#UNIDADE
#DEZENA
#CENTENA
#MILHAR

n = 0
while n != 1:
    num = str(input('Informe um número inteiro de 0 à 9999:\n'))
    if len(num) == 4 and int(num) >= 0 and int(num) <= 9999:
        print('Unidade: {}'.format(num[3]))
        print('Dezena: {}'.format(num[2]))
        print('Centena: {}'.format(num[1]))
        print('Milhar: {}'.format(num[0]))
        n = 1
    elif len(num) == 3 and int(num) >= 0 and int(num) <= 9999:
        print('Unidade: {}'.format(num[2]))
        print('Dezena: {}'.format(num[1]))
        print('Centena: {}'.format(num[0]))
        n = 1
    elif len(num) == 2 and int(num) >= 0 and int(num) <= 9999:
        print('Unidade: {}'.format(num[1]))
        print('Dezena: {}'.format(num[0]))
        n = 1
    elif len(num) == 1 and int(num) >= 0 and int(num) <= 9999:
        print('Unidade: {}'.format(num[0]))
        n = 1
    else:
        print('Valor inválido!')
        n = 0
