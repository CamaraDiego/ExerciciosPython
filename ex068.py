#JOGAR PAR OU IMPAR
#PARAR QUANDO O USUARIO PERDER
#MOSTRAR O TOTAL DE VITORIAS CONSECUTIVAS NO FINAL
from time import sleep
from random import randint
print('-=-' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 10)
vitorias = 0
while True:
    computador = randint(0, 10)
    escolha = str(input('Você escolhe Par ou Ímpar? [P/I]: ')).upper()
    print('-=-' * 10)
    while ((escolha in 'PI') == False) or (escolha.isspace() == True):
        escolha = str(input('Opção inválida, digite P para Par ou I para Ímpar: ')).upper()
        print('-=-' * 10)
    usuario = str(input('Digite um número inteiro: ')).strip()
    print('-=-' * 10)
    while usuario.isnumeric() == False:
        usuario = str(input('Valor inválido, digite um número inteiro: ')).strip()
        print('-=-' * 10)
    usuario = int(usuario)
    parouimpar = computador + usuario
    print('Par...', end='')
    sleep(0.5)
    print('ou...', end='')
    sleep(0.5)
    print('ímpar!')
    print('-=-' * 10)
    sleep(0.5)
    if escolha == 'P':
        print(f'Você escolheu PAR e jogou o número {usuario}.')
        sleep(1)
        print(f'Eu sou ímpar e joguei o número {computador}.')
        sleep(1)
        if parouimpar == 0:
            print(f'{computador} + {usuario} = {parouimpar}que é um número neutro, empatamos!')
            print('-=-' * 10)
            sleep(0.5)
        elif parouimpar % 2 == 0 and parouimpar != 0:
            print(f'{computador} + {usuario} = {parouimpar} que é PAR, você ganhou!')
            print('-=-' * 10)
            sleep(0.5)
            vitorias += 1
        elif parouimpar % 2 != 0 and parouimpar != 0:
            print(f'{computador} + {usuario} = {parouimpar} que é ÍMPAR, você perdeu!')
            sleep(0.5)
            break
    elif escolha == 'I':
        print(f'Você escolheu ÍMPAR e jogou o número {usuario}.')
        sleep(1)
        print(f'Eu sou par e joguei o número {computador}.')
        sleep(1)
        if parouimpar == 0:
            print(f'{computador} + {usuario} = {parouimpar}que é um número neutro, empatamos!')
            print('-=-' * 10)
            sleep(0.5)
        elif parouimpar % 2 == 0 and parouimpar != 0:
            print(f'{computador} + {usuario} = {parouimpar} que é PAR, você perdeu!')
            sleep(0.5)
            break
        elif parouimpar % 2 != 0 and parouimpar != 0:
            print(f'{computador} + {usuario} = {parouimpar} que é ÍMPAR, você ganhou!')
            print('-=-' * 10)
            sleep(0.5)
            vitorias += 1
print('-=-' * 10)
print(f'Neste jogo você obteve {vitorias} vitorias consecutivas.')
