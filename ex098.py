#FUNÇÃO CHAMADA CONTADOR
#PRIMEIRO CONTAR AUTOMATICAMENTE DE 1 ATÉ 10 DE 1 EM 1
#SEGUNDO CONTAR DE 10 ATÉ 0 DE 2 EM 2
#POR FIM PERGUNTAR AO USUARIO O INICIO FIM E PASSO (CONTAGEM PERSONALIZADA)
#O PASSO DEVE FUNCIONAR MESMO QUE SEJA DIGITADO VALOR NEGATIVO (MODULO)
#CASO SEJA DIGITADO 0 NO PASSO DEVE FUNCIONAR DE 1 EM 1

def usuario(g, h, i):
    from time import sleep
    print('-' * 20)
    if i == 0 and h > g:
        i = 1
    elif i == 0 and h < g:
        i = -1
    if i < 0 and h > g:
        i = abs(i)
    if i > 0 and h < g:
        i = i * (-1)
    if h > g:
        for j in range(g, h + 1, i):
            print(j, end=' ')
            sleep(0.5)
    if h < g:
        for j in range(g, h - 1, i):
            print(j, end=' ')
            sleep(0.5)
    print()
    sleep(0.5)
    print('-' * 20)
    print(f'{"FIM DO PROGRAMA":^21}')
    print('-' * 20)

def contador(a, b, e, f):
    from time import sleep
    print('-' * 20)
    for c in range(a, b):
        print(c, end = ' ')
        sleep(0.5)
    print()
    print('-' * 20)
    for d in range(e, f, -2):
        print(d, end = ' ')
        sleep(0.5)
    print()
    print('-' * 20)
    usuario(g=int(input('Qual o início: ')),
            h=int(input('Qual o fim: ')),
            i=int(input('Qual o passo: ')))
    print()
    sleep(0.5)


contador(1, 11, 10, -1)
