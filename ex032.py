#LER UM ANO
#DIZER SE É UM ANO BISSEXTO
from datetime import date
ano = str(input('Informe o ano que quer analisar:\n')).strip()
ano = int(ano)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
