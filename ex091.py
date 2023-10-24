#QUATRO JOGADORES JOGAM UM DADO COM RESULTADOS ALEATÓRIOS
#GUARDAR OS RESULTADOS EM UM DICIONÁRIO
#COLOCAR O DICIONÁRIO EM ORDEM
#O VENCEDOR É QUE TIROU O MAIOR RESULTADO
"NÃO FOI DADOS OS MEIOS PARA A RESOLUÇÃO EM AULA, ASSISTIR VÍDEO DA RESOLUÇÃO"
from random import randint
from operator import itemgetter
from time import sleep
dicionario = dict()
for c in range(1, 5):
    dicionario[f'Jogador {c}'] = randint(1, 6)
    print(f'O jogador {c} tirou {dicionario[f"Jogador {c}"]} no dado.')
    sleep(0.5)
classificacao = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print('-=-' * 10)
for pos, valor in enumerate(classificacao):
    print(f'{pos + 1}º lugar: {valor[0]} tirou {valor[1]}.')
    sleep(0.5)
