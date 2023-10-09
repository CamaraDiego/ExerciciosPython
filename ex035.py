#LER TRES COMPRIMENTOS
#DIZER SE PODE FORMAR UM TRIÂNGULO COM ESSES COMPRIMENTOS
m1 = str(input('Informe a primeira medida:\n')).strip()
m1 = float(m1)
m2 = str(input('Informe a segunda medida:\n')).strip()
m2 = float(m2)
m3 = str(input('Informe a terceira medida:\n')).strip()
m3 = float(m3)
if (abs(m1 - m2) < m3 < m1 + m2) and (abs(m1 - m3) < m2 < m1 + m3) and (abs(m2 - m3) < m1 < m2 + m3):
    print('É possível formar um triângulo com as medidas {:.2f}, {:.2f} e {:.2f}.'.format(m1, m2, m3))
else:
    print('Não é possível formar um triângulo com as medidas {:.2f}, {:.2f} e {:.2f}.'.format(m1, m2, m3))
