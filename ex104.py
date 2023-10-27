#FUNÇÃO LEIAINT
#SEMELHANTE AO INPUT MAS ACEITANDO APENAS VALOR NUMÉRICO

def leiaint(num):
    while True:
        if num.isnumeric():
            return int(num)
        else:
            print('\033[1;31mERRO! VALOR INVÁLIDO\033[m')
            num = str(input('Digite um número inteiro: '))


numero = leiaint(str(input('Digite um número inteiro: ')))
print(f'Você digitou o número inteiro: {numero}')
