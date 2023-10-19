#CRIAR PALPITES PARA A MEGA SENA
#PERGUNTAR QUANTOS JOGOS SERÃO FEITOS
#GERAR 6 NUMEROS ENTRE 1 E 60 SEM REPETIÇÕES PARA CADA JOGO
#CADASTRAR TUDO EM UMA LISTA COMPOSTA
from random import randint
from time import sleep
lista = list()
jogos = list()
quant = int(input('Quantos jogos quer que sorteie?: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'SORTEANDO {quant} JOGOS')
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('BOA SORTE')
