dias = int(input('Quantos dias alugados?\n'))
kms = float(input('Quantos Kms rodados?\n'))
preco = dias * 60 + kms * 0.15
print('O preço a ser pago por {} dias e {:.2f} kms é de R${:.2f}.'.format(dias, kms, preco))
