#LER DOIS VALORES INTEIROS E EXIBIR O MENU
#[1] SOMAR
#[2] MULTIPLICAR
#[3] MAIOR
#[4] NOVOS NÚMEROS
#[0] SAIR DO PROGRAMA
print('===================================')
print('OPERAÇÕES COM DOIS NÚMEROS INTEIROS')
print('===================================')
n1 = str(input('Informe o primeiro número: ')).strip()
while (n1.isnumeric() == False) and (n1.replace('.', '').isnumeric() == False):
    n1 = str(input('Informe um valor numérico para o primeiro número: ')).strip()
n2 = str(input('Informe segundo número: ')).strip()
while n2.isnumeric() == False and (n2.replace('.', '').isnumeric() == False):
    n2 = str(input('Informe um valor numérico para o segundo número: ')).strip()
print('===================================')
n1 = float(n1)
n2 = float(n2)
maior = 0
if n1 > n2:
    maior = n1
else:
    maior = n2
op = str(input("""Digite qual operação deseja prosseguir com estes valores:
[1] SOMA
[2] MULTIPLICAÇÃO
[3] QUAL O MAIOR
[4] NOVOS NÚMEROS
[0] SAIR DO PROGRAMA\n""")).strip()
print('===================================')
while (op.isnumeric() == False) or (int(op) != 1 and int(op) != 2 and int(op) != 3 and int(op) != 4 and int(op) != 0):
    print('== AÇÃO INVÁLIDA ==')
    op = str(input("""Digite qual operação deseja prosseguir com estes valores:
[1] SOMA
[2] MULTIPLICAÇÃO
[3] QUAL O MAIOR
[4] NOVOS NÚMEROS
[0] SAIR DO PROGRAMA\n""")).strip()
    print('===================================')
while int(op) != 0:
    if int(op) == 1:
        print('A soma entre {} e {} é {}.'.format(n1, n2, n1 + n2))
        print('===================================')
    elif int(op) == 2:
        print('O valor da multiplicação {}x{} = {}.'.format(n1, n2, n1 * n2))
        print('===================================')
    elif int(op) == 3:
        print('Entre os números digitados o maior é {}.'.format(maior))
        print('===================================')
    elif int(op) == 4:
        n1 = str(input('Informe o primeiro número: ')).strip()
        while (n1.isnumeric() == False) and (n1.replace('.', '').isnumeric() == False):
            n1 = str(input('Informe um valor numérico para o primeiro número: ')).strip()
        n2 = str(input('Informe segundo número: ')).strip()
        while n2.isnumeric() == False and (n2.replace('.', '').isnumeric() == False):
            n2 = str(input('Informe um valor numérico para o segundo número: ')).strip()
        print('===================================')
        n1 = int(n1)
        n2 = int(n2)
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
    op = str(input("""Digite qual operação deseja prosseguir com estes valores:
[1] SOMA
[2] MULTIPLICAÇÃO
[3] QUAL O MAIOR
[4] NOVOS NÚMEROS
[0] SAIR DO PROGRAMA\n""")).strip()
    print('===================================')
    while (op.isnumeric() == False) or (int(op) != 1 and int(op) != 2 and int(op) != 3 and int(op) != 4 and int(op) != 0):
        print('== AÇÃO INVÁLIDA ==')
        op = str(input("""Digite qual operação deseja prosseguir com estes valores:
[1] SOMA
[2] MULTIPLICAÇÃO
[3] QUAL O MAIOR
[4] NOVOS NÚMEROS
[0] SAIR DO PROGRAMA\n""")).strip()
        print('===================================')
print('Muito obrigado por usar nosso APP.')
print('===================================')
