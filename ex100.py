#DUAS FUNÇÕES
#UMA CHAMADA SORTEIA QUE VAI SORTEAR 5 NÚMEROS ALEATÓRIOS E COLOCAR DENTRO DE UMA LISTA
#OUTRA CHAMADA SOMAPAR QUE VAI SOMAR TODOS OS VALORES PARES

def sorteia(a):
    """
    SORTEAMENTO DE 5 NÚMEROS ALEATÓRIOS ENTRE 0 E 100,
    EXIBE EM TELA OS NÚMEROS SORTEADOS E INSERE SEUS VALORES EM UMA LISTA
    :param a: lista onde serão inseridos os números sorteados
    :return:
    """
    from random import randint
    from time import sleep
    print('-' * 45)
    print('Sorteando 5 números aleatórios entre 0 e 100')
    for c in range(1, 6):
        n = randint(0, 100)
        a.append(n)
        print(n, end=' ')
        sleep(0.5)
    print()
    print('-' * 45)


def somapar(b):
    from time import sleep
    soma = 0
    for c in b:
        if c % 2 == 0:
            soma += c
    sleep(0.5)
    print('A soma dos valores pares neste conjunto é: ', end = '')
    sleep(0.5)
    print(soma)
    print('-' * 45)


lista = list()
sorteia(lista)
somapar(lista)
