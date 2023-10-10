#LER A DATA DE NASCIMENTO
#INFORMAR SE AINDA VAI SE ALISTAR E QUANTO TEMPO
#SE É HORA DE SE ALISTAR
#SE JA PASSOU DA HORA DE SE ALISTAR E QUANTO TEMPO

from datetime import date
nasc = str(input('Informe seu ano de nascimento: ')).strip()
nasc = int(nasc)
idade = date.today().year - nasc
if idade < 18:
    falta = 18 - idade
    print('Ainda faltam {} anos para que você precise se alistar.'.format(int(falta)))
elif idade == 18:
    print('Você está em ano de alistamento militar!')
else:
    passou = idade - 18
    print('Você já deveria ter se alistado à {} anos atrás.'.format(int(passou)))
