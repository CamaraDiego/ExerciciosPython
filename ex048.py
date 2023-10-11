#CALCULAR A SOMA ENTRE TODOS OS NÚMEROS ÍMPARES MULTIPLOS DE 3 ENTRE 1 E 500

contador = soma = 0
print('Entre 1 e 500 os números ímpares divisiveis por 3 são:')
for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end = ' ')
        soma = soma + c
        contador = contador + 1
print('\nO somatório destes valores é {}.'.format(soma))
print('Ao todo foram somados {} valores.'.format(contador))
