#LER UMA FRASE QUALQUER
#DIZER SE É UM PALÍNDROMO

print('Verificando palíndromos')
frase = str(input('Digite uma frase:\n')).strip()
frase2 = frase.upper().split()
frase2 = ''.join(frase2)
frase3 = ''
for c in range(len(frase2) - 1, -1, -1):
    frase3 = frase3 + frase2[c]
if frase2 == frase3:
    print('A frase "{}" é um palíndromo'.format(frase))
else:
    print('A frase "{}" não é um palíndromo.'.format(frase))
