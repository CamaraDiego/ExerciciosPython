#FUNÇÃO CHAMADA MAIOR
#RECEBER VARIOS PARAMETROS COM VALORES INTEIROS
#ANALISAR E DIZER QUAL DELES É O MAIOR

def maior(* num):
    from time import sleep
    maior = cont = 0
    print('Analisando os valores inseridos:')
    for c in num:
        print(c, end = ' ')
        sleep(0.5)
        if cont == 0 or c > maior:
            maior = c
        cont += 1
    print()
    print(f'Ao todo foram inseridos {len(num)} números.')
    sleep(0.5)
    print(f'Entre eles o maior é o {maior}.')
    sleep(0.5)
    print('-' * 35)
    sleep(0.5)


print('-' * 35)
maior(22, 3, 5, 8, 14, 0)
maior(0, 5, 85, 47, 92)
maior(15, 23, 65, 12, 35)
