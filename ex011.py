la = float(input('Informe a largura da parede em metros: '))
al = float(input('Informe a altura da parede em metros: '))
area = la * al
t = area / 2
print('Para {:.2f} metros quadrados você vai precisar de pelo menos {:.2f} lata(s) de tinta'.format(area, t))
