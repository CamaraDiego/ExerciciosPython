#UMA TUPLA COM OS 20 TIMES DA SÉRIE A DO BRASILEIRÃO
#MOSTRAR OS 5 PRIMEIROS COLOCADOS
#MOSTRAR OS 4 ÚLTIMOS COLOCADOS
#LISTA COM OS TIMES EM ORDEM ALFABÉTICA
#MOSTRAR EM QUE POSIÇÃO ESTÁ CUIABÁ
from time import sleep
classificacao = ('Botafogo', 'Bragantino', 'Gremio', 'Palmeiras', 'Flamengo',
                 'Fortaleza', 'Fluminense', 'Athletico-PR', 'Atlético-MG', 'São Paulo',
                 'Cuiabá', 'Internacional', 'Cruzeiro', 'Corinthians', 'Santos',
                 'Bahia', 'Vasco', 'Goiás', 'Coritiba', 'América-MG')
#cuiaba = classificacao.index('Cuiabá') + 1
print('-=-' * 13)
sleep(0.5)
print(f'Os 5 primeiros colocados na tabela são:\n{classificacao[:5]}')
print('-=-' * 13)
sleep(0.5)
print(f'Os 4 últimos colocados na tabela são:\n{classificacao[-4:]}')
print('-=-' * 13)
sleep(0.5)
print(f'Os times em ordem alfabética:\n{sorted(classificacao)}')
print('-=-' * 13)
sleep(0.5)
print(f'E o time do Cuiabá está na {classificacao.index("Cuiabá") + 1}ª colocação.')
