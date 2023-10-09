n1 = float(input('Digite a primeira nota:\n'))
n2 = float(input('Digite a segunda nota:\n'))
m = (n1 + n2) / 2
print('Sua média é {:.2f}.'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim, estude mais!')
