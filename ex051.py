#LER O PRIMEIRO TERMO E A RAZÃO DE UMA PROGRESSÃO ARITMÉTICA
#MOSTRAR OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO
print('Vamos fazer uma progressão aritmética')
termo = str(input('Digite o primeiro termo: ')).strip()
termo = int(termo)
razao = str(input('Digite a razão: ')).strip()
razao = int(razao)
print('Os 10 primeiros termos desta progressão aritmética são:')
for c in range(termo, termo + (razao * 10), razao):
    print(c, end =' ')
