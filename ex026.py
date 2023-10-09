#LER UMA FRASE
#QUANTAS VEZES APARECE A LETRA A
#EM QUE POSIÇÃO APARECE A PRIMEIRA VEZ
#EM QUE POSIÇÃO APARECE NA ÚLTIMA VEZ
frase = str(input('Digite uma frase:\n')).strip().upper()
if frase.count('A') >= 1:
    print('Nessa frase aparece {} vezes a letra "A".'.format(frase.count('A')))
    print('Essa letra aparece primeiro na posição {}.'.format(frase.find('A') + 1))
    print('E por último na posição {}.'.format(frase.rfind('A') + 1))
else:
    print('Nessa frase não tem a letra "A"')
