#CRIAR UMA MATRIZ 3X3
#PREENCHER OS VALORES COM DADOS DIGITADOS NO TECLADO
#EXIBIR A MATRIZ COM OS VALORES
#EXIBIR TAMBEM
#A SOMA DE TODOS OS VALORES PARES DIGITADOS
#A SOMA DOS VALORES DA TERCEIRA COLUNA
#O MAIOR VALOR DA SEGUNDA LINHA
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=-' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end = '')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos valores pares é {spar}.')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores na terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c]:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')
