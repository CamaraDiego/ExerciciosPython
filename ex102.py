#FUNÇÃO FATORIAL
#PARAMETRO NUMERAL PARA CALCULAR SEU FATORIAL (N)
#PARAMETRO PARA MOSTRAR OU NÃO O CÁLCULO (SHOW=FALSE)

def fatorial(n, show=False):
    neutro = 1
    for c in range(1, n + 1, 1):
        neutro *= c
        if (show == True) and (c != n ):
            print(f'{c} x ', end = '')
        if (show == True) and (c == n):
            print(f'{c} = {neutro}')
    if show == False:
        print(f'O fatorial de {n} é {neutro}.')


numero = fatorial(int(input('Digite um númeor inteiro para seu fatorial: ')))
