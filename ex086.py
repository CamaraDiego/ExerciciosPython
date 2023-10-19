#CRIAR UMA MATRIZ 3X3
#PREENCHER OS VALORES COM DADOS DIGITADOS NO TECLADO
#EXIBIR A MATRIZ COM OS VALORES
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=-' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end = '')
    print()
