#LER UM NUMERO INTEIRO
#USUARIO ESCOLHER QUAL BASE DE CONVERSAO
#1 BINARIO
#2 OCTAL
#3 HEXADECIMAL
#FAZER A CONVERSAO

n = str(input('Informe um número inteiro: ')).strip()
n = int(n)
print('Deseja usar qual base de conversão:')
o = int(input("""1. BINÁRIO
2. OCTAL
3. HEXADECIMAL\n"""))
if o == 1:
    print('O número {} convertido para binário é {}.'.format(n, bin(n)[2:]))
elif o == 2:
    print('O número {} convertido para octal é {}.'.format(n, oct(n)[2:]))
elif o == 3:
    print('O número {} convertido para hexadecimal é {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida.')
