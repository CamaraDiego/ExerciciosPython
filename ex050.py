#LER 6 NÚMEROS INTEIROS
#EXIBIR A SOMA DOS NÚMEROS PARES DIGITADOS APENAS
#DESCONSIDERAR OS ÍMPARES

s = 0
for c in range(1, 7):
    n = str(input('Digite o {}º número inteiro: '.format(c))).strip()
    n = int(n)
    if n % 2 == 0:
        s = s + n
print('O somatório dos valores PARES digitados é {}.'.format(s))
