#LER SALÁRIO
#PARA SUPERIORES A R$1250 UM AUMENTO DE 10%
#PARA INFERIORES OU IGUAIS A R$1250 AUMENTO DE 15%
sal = str(input('Informe o salário em R$')).strip()
sal = float(sal)
if sal > 1250:
    aum = sal * 1.10
else:
    aum = sal * 1.15
print('O novo salário será de R${:.2f}.'.format(aum))
