#LER A VELOCIDADE DE UM CARRO
#SE ULTRAPASSAR 80KM/H DIZER QUE FOI MULTADO
#CUSTO DE R$7 POR CADA KM ACIMA DO LIMITE
vel = str(input('Informe a velocidade do carro em KM/h:\n')).strip()
vel = float(vel)
if vel > 80:
    m = (vel - 80) * 7
    print('Você está acima do limite permitido e será multado.')
    print('DIRIJA COM RESPONSABILIDADE!')
    print('O custo da sua multa é de R${:.2f}.'.format(m))
else:
    print('Você está dentro do limite permitido.')
