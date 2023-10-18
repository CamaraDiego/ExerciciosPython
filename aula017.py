valores = list()
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for pos, valor in enumerate(valores):
    print(f'Na posição {pos + 1} tem o valor {valor}.')
