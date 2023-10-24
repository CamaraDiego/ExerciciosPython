#APRIMORAR O 93
#FUNCIONAR COM VÁRIOS JOGADORES
from time import sleep
dicionario = dict()
gols = list()
jogadores = list()
codigo = 1
print('-=-' * 15)

while True:
    dicionario['código'] = codigo
    dicionario['jogador'] = str(input('Nome do jogador: ')).strip()
    print('-=-' * 15)
    partidas = int(input(f'Quantas partidas {dicionario["jogador"]} jogou? '))
    print('-=-' * 15)

    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na {c}ª partida? ')))

    dicionario['gols'] = gols[:]
    dicionario['total'] = sum(gols)
    jogadores.append(dicionario.copy())
    gols.clear()
    codigo += 1
    print('-=-' * 15)

    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break

print('-=-' * 15)
print(f'{"cod":<4}{"nome":<15}{"gols":<20}{"total":<}')
print('-' * 50)

for valor in jogadores:
    print(f'{valor["código"]:>3} {valor["jogador"]:<15}{str(valor["gols"]):<20}{valor["total"]:<}')
print('-' * 50)

while True:
    escolha = int(input('Mostrar dados de qual jogador? (digite o código ou 0 para parar): '))

    if escolha == 0:
        break

    for valor in jogadores:
        if escolha == valor['código']:
            print(f'Levantamento do jogador {valor["jogador"]}:')

            for c in range(0, len(valor['gols'])):
                print(f'No {c + 1}º jogo fez {valor["gols"][c]} gols.')

    print('-' * 50)
