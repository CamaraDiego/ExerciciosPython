#LER O ANO DE NASCIMENTO DE 7 PESSOAS
#MOSTRAR QUANTAS NÃO ATINGIRAM A MAIORIDADE E QUANTAS JÁ SÃO MAIORES

from datetime import date
menor = maior = 0
for c in range(1, 8):
    ano = str(input('Informe o ano um ano de nascimento: ')).strip()
    ano = int(ano)
    if (date.today().year - ano) < 18:
        menor = menor + 1
    else:
        maior = maior + 1
print('Neste grupo existem {} pessoas em minoridade e {} pessoas em maioridade.'.format(menor, maior))
