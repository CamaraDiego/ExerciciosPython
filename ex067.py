#MOSTRAR A TABUADA DE NÚMEROS SOLICITADOS
#PARAR QUANDO O VALOR INSERIDO FOR NEGATIVO
while True:
    num = str(input('Informe um número inteiro para tabuada ou negativo para sair: ')).strip()
    while num.isnumeric() == False and num.replace('-', '').isnumeric() == False:
        num = str(input('Valor inválido digitado\nInforme um número inteiro para tabuada ou negativo para sair: ')).strip()
    num = int(num)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {num} = {c * num}')
    print('-=-' * 10)
print('-=-' * 10)
print('Obrigado por usar nosso APP.')
