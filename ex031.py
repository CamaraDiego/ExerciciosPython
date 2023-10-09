#PERGUNTAR A DISTANCIA DE UMA VIAGEM EM KM
#CALCULAR O PREÇO DA PASSAGEM
#R$0.50 POR KM ATÉ 200KM
#R$0.45 POR KM ACIMA DISSO

dist = str(input('Informe a distância total da viagem em KM:\n')).strip()
dist = float(dist)
if dist <= 200:
    p = dist * 0.50
else:
    p = dist * 0.45
print('Para uma viagem de {:.2f}KM o preço da passagem é de R${:.2f}.'.format(dist, p))
