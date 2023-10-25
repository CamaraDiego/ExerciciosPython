#UMA FUNÇÃO CHAMADA AREA
#RECEBA AS DIMENSÕES RETANGULARES DE UM TERRENO
#MOSTRAR A AREA DO TERRENO
def area(a, b):
    area = a * b
    print(f'A área de um terreno {a:.2f}(m) x {b:.2f}(m) é igual a {area:.2f}m2')


a = float(input('Primeira medida em metro: '))
b = float(input('Segunda medida em metro: '))
area(a, b)
