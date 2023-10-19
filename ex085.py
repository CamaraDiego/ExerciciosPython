#LER SETE VALORES NUMERICOS (USAR SO UMA LISTA PARA TUDO)
#CADASTRAR EM LISTA UNICA MANTENDO SEPARADOS OS VALORES PARES DOS IMPARES
#NO FINAL MOSTRAR OS VALORES PARES E IMPARES SEPARADOS E EM ORDEM CRESCENTE
num = [[], []]
for c in range(1, 8):
    valor = int(input('Insira um número: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares são {num[0]}')
print(f'Os valores impares são {num[1]}')
