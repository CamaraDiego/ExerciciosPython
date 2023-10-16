#CRIAR UMA TUPLA COM VÁRIAS PALAVRA (NÃO USAR ACENTUAÇÃO)
#MOSTRAR PARA CADA PALAVRA AS SUAS VOGAIS
from time import sleep
tupla = ('Redemoinho', 'Afiado', 'Couro', 'Embaixador',
         'Arquiteto', 'Puberdade', 'Imortal')
print('=' * 35, end = '')
print('\n', end = '')
sleep(0.5)
for palavra in tupla:
    print(f'A palavra {palavra} contém as vogais:')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            sleep(0.5)
            print(letra.upper(), end = ' ')
    sleep(0.5)
    print('\n', end = '')
    print('=' * 35)
    sleep(0.5)
