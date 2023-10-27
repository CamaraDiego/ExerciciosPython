#FUNÇÃO FICHA
#DOIS PARAMETROS OPCIONAIS
#NOME DO JOGADOR
#QUANTOS GOLS MARCOU
#INFORMA A FICHA DO JOGADOR MESMO QUE UM DOS VALORES NÃO SEJA INFORMADO
#<DESCONHECIDO> E 0
def ficha(j, g):
    print(f'O jogador {j} fez {g} gols')


jogador = str(input('Digite o nome do jogador: ')).strip()
if jogador == '':
    jogador = '<desconhecido>'
gols = str(input('Digite a quantidade de gols: ')).strip()
if gols == '':
    gols = 0
elif gols.isnumeric():
    gols = int(gols)

ficha(jogador, gols)
