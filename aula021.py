def soma1(a, b, c = 0):
    """
    SOMA ATÉ TRÊS VALORES INFORMADOS, SENDO 2 OBRIGATÓRIOS E 1 OPCIONAL
    :param a:primeiro valor
    :param b:segundo valor
    :param c:terceiro valor, sendo opcional
    :return:
    """
    s = a + b + c
    print(f'A soma vale {s}')

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A vale {a}')


#PROGRAMA PRINCIPAL
a = 5
teste(a)

def soma(a = 0, b = 0, c = 0):
    """
    SOMA ATÉ TRÊS VALORES INFORMADOS, SENDO 2 OBRIGATÓRIOS E 1 OPCIONAL
    :param a:primeiro valor
    :param b:segundo valor
    :param c:terceiro valor, sendo opcional
    :return:
    """
    s = a + b + c
    return s


resp1 = soma(3, 2, 5)
resp2 = soma(1, 7)
resp3 = soma(6)
print(f'As somas valem {resp1}, {resp2} e {resp3}.')

def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par.')
else:
    print('É ímpar.')
