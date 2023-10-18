#LER 5 VALORES NUMERICOS E GUARDAR EM UMA LISTA
#MOSTRAR QUAL O MAIOR E O MENOR VALORES
#E MOSTRA AS SUAS POSIÇÕES NA LISTA
#maior = menor = 0
valores = list()
for c in range(0, 5):
    valor = str(input(f'Insira o {c +1}º número inteiro e maior ou igual à zero: ')).strip()
    while valor.isnumeric() == False:
        valor = str(input(f'Valor inválido, insira o {c +1}º número inteiro e maior ou igual à zero: ')).strip()
    valor = int(valor)
    valores.append(valor)
posmenor = list()
posmaior = list()
for pos, valor in enumerate(valores):
    if valor == min(valores):
        posmenor.append(pos + 1)
    if valor == max(valores):
        posmaior.append(pos + 1)
print(valores)
print(f'O menor valor digitado foi {min(valores)} que está nas posições {posmenor}.')
print(f'O maior valor digitado foi {max(valores)} que está nas posições {posmaior}.')
