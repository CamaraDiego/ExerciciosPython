#RECEBER NOME DE UM JOGADOR
#RECEBER QUANTIDADE DE PARTIDAS
#RECEBER QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA
#GUARDAR TUDO EM UM DICIONÁRIO INCLUÍNDO O TOTAL DE GOLS
#EXIBIR NO FINAL O NOME DO JOGADOR E O TOTAL DE PARTIDAS
#QUANTAS GOLS FEZ EM CADA PARTIDA
#E O TOTAL DE GOLS
from time import sleep
dicionario = dict()
print('-=-' * 15)
dicionario['jogador'] = str(input('Nome do jogador: ')).strip()
print('-=-' * 15)
partidas = int(input(f'Quantas partidas {dicionario["jogador"]} jogou? '))
print('-=-' * 15)
gols = list()
for c in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na {c}ª partida? ')))
dicionario['gols'] = gols[:]
dicionario['total'] = sum(gols)
print('-=-' * 15)
sleep(0.5)
print(dicionario)
sleep(0.5)
print('-=-' * 15)
for k, v in dicionario.items():
    print(f'O campo {k} tem o valor {v}.')
    sleep(0.5)
print('-=-' * 15)
sleep(0.5)
print(f'O jogador {dicionario["jogador"]} jogou {len(dicionario["gols"])} partidas.')
sleep(0.5)
for pos, valor in enumerate(gols):
    print(f'=> Na partida {pos + 1}, fez {valor} gols.')
    sleep(0.5)
print(f'Foi um total de {dicionario["total"]} gols.')
print('-=-' * 15)
