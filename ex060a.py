#LER UM NÚMERO QUALQUER E MOSTRAR SEU FATORIAL
print('VERIFICADOR DE FATORIAL')
n1 = str(input('Informe um número inteiro: ')).strip()
while n1.isnumeric() == False:
    n1 = str(input('Valor inválido, informe um número inteiro: '))
n1 = int(n1)
c = f = 1
while c <= n1:
    f = f * c
    c += 1
print('O resultado de {}! = {}.'.format(n1, f))
