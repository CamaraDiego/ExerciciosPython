#CONTAGEM REGRESSIVA PARA ESTOURO DE FOGOS
#DE 5 ATÉ 0
#PAUSA DE 1 SEGUNDO ENTRE ELES

import django
from time import sleep
print('CONTAGEM REGRESSIVA')
sleep(1)
for c in range(5, -1, -1):
    if c != 0:
        print(c)
        sleep(1)
    if c == 0:
        print(c)
print('🎆🧨🎉🎊🎇')
