#LER VARIOS NUMEROS INTEIROS
#PARAR QUANDO O USUARIO DIGITAR 999
#MOSTRAR QUANTOS NUMEROS FORAM DIGITADOS E O SOMATORIO
cont = soma = c = 0
print('-=-' * 15)
while c != 999:
    c = str(input('Digite um número ou 999 para sair: ')).strip()
    while c.isnumeric() == False and c.replace('.', '').isnumeric() == False:
        c = str(input('Valor inválido, digite um número ou 999 para sair: '))
    c = float(c)
    if c != 999:
        soma += c
        cont += 1
print('-=-' * 15)
print('Foram digitados {:.0f} números.'.format(cont))
print('O somatório dos valores digitados é {:.2f}.'.format(soma))
print('-=-' * 15)
print('Obrigado por usar nosso APP.')
