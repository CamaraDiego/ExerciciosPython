#JOGAR JOKENPO COM A MAQUINA
from random import randint
from time import sleep
print('VAMOS JOGAR JOKENPO')
usuario = str(input("""1. PEDRA
2. PAPEL
3. TESOURA\n""")).strip()
usuario = int(usuario)
maquina = randint(1, 3)
print('JO...', end='')
sleep(1)
print('KEN...',end='')
sleep(1)
print('PO!')
sleep(1)
if usuario == 1 and maquina == 3:
    print("""Você: PEDRA
EU: TESOURA
PARABÉNS, VOCÊ VENCEU!""")
elif usuario == 1 and maquina == 2:
    print("""Você: PEDRA
EU: PAPEL
EU VENCI!""")
elif usuario == 2 and maquina == 1:
    print("""Você: PAPEL
EU: PEDRA
PARABÉNS, VOCÊ VENCEU!""")
elif usuario == 2 and maquina == 3:
    print("""Você: PAPEL
EU: TESOURA
EU VENCI!""")
elif usuario == 3 and maquina == 2:
    print("""Você: TESOURA
EU: PAPEL
PARABÉNS, VOCÊ VENCEU!""")
elif usuario == 3 and maquina == 1:
    print("""Você: TESOURA
EU: PEDRA
EU VENCI!""")
elif usuario == maquina:
    if usuario == maquina == 1:
        print('Ambos escolhemos PEDRA, portanto empatamos!')
    elif usuario == maquina == 2:
        print('Ambos escolhemos PAPEL, portanto empatamos!')
    elif usuario == maquina == 3:
        print('Ambos escolhemos TESOURA, portanto empatamos!')
print('FIM')