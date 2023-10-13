#COMPUTADOR PENSAR EM UM NÚMERO ENTRE 0 E 10
#USUARIO TENTAR ADIVINHAR
#CONTINUAR RODANDO ENQUANTO NÃO ADIVINHA
#QUANDO ADIVINHAR MOSTRAR QUANTAS TENTATIVAS FORAM NECESSÁRIAS

from random import randint
computador = randint(0, 10)
cont = 1
print('TENTE ADIVINHAR QUE NÚMERO INTEIRO ENTRE 0 E 10 ESTOU PENSANDO')
usuario = str(input('Informe um número: ')).strip()
usuario = int(usuario)
while usuario != computador:
    cont += 1
    if usuario > computador:
        usuario = str(input('Errado, tente um número menor...'))
        usuario = int(usuario)
    else:
        usuario = str(input('Errado, tente um número maior...'))
        usuario = int(usuario)
print('Meus parabéns, eu realmente pensei no número {}.'.format(computador))
print('Você precisou de {} tentativas para acertar.'.format(cont))
