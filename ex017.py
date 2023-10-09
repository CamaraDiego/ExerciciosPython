from math import hypot
co = float(input('Informe o comprimento do Cateto Oposto: '))
ca = float(input('Informe o comprimento do Cateto Adjascente: '))
hi = hypot(co, ca)
print('A hipotenusa deste triângulo mede {:.2f}'.format(hi))
