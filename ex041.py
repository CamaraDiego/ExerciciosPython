#LER A DATA DE NASCIMENTO DE UM ATLETA
#MOSTRAR A CATEGORIA DE ACORDO COM A IDADE
#ATE 9 ANOS MIRIM
#ATE 14 INFANTIL
#ATE 19 JUNIOR
#ATE 25 SENIOR
#ACIMA MASTER

from datetime import date
nasc = str(input('Informe o ano de nascimento do atleta: ')).strip()
nasc = int(nasc)
idade = date.today().year - nasc
if idade <= 9:
    print('O atleta de {} anos competirá na categoria MIRIM.'.format(idade))
elif 9 < idade <= 14:
    print('O atleta de {} anos competirá na categoria INFANTIL.'.format(idade))
elif 14 < idade <= 19:
    print('O atleta de {} anos competirá na categoria JUNIOR.'.format(idade))
elif 19 < idade <= 25:
    print('O atleta de {} anos competirá na categoria SENIOR.'.format(idade))
else:
    print('O atleta de {} anos competirá na categoria MASTER.'.format(idade))
