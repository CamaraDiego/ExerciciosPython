#LER ALTURA E PESO
#CALCULAR IMC
#ABAIXO DE 18.5: ABAIXO DO PESO
#ENTRE 18.5 25: PESO IDEAL
#25 ATE 30: SOBREPESO
#30 ATE 40:OBESIDADE
#ACIMA DE 40: OBESIDADE MORBIDA

from math import pow
altura = str(input('Informe a altura em metros: ')).strip()
altura = float(altura)
peso = str(input('Informe o peso em KG: ')).strip()
peso = float(peso)
imc = peso / (pow(altura, 2))
print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está na classificação MAGREZA.')
elif 18.5 <= imc < 25:
    print('Você está na classificação NORMAL.')
elif 25 <= imc < 30:
    print('Você está na classificação SOBREPESO.')
elif 30 <= imc < 35:
    print('Você está na classificação OBESIDADE GRAU I.')
elif 35 <= imc <= 40:
    print('Você está na classificação OBESIDADE GRAU II.')
elif 40 < imc:
    print('Você está na classificação OBESIDADE GRAU III.')
