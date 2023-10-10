#PEDIR 3 COMPRIMENTOS
#DIZER SE PODE SE FORMAR UM TRIANGULO COM ESSES COMPRIMENTOS
#INFORMAR O TIPO DE TRIANGULO
#EQUILATERO: TODOS OS LADOS IGUAIS
#ISOCELES: DOIS LADOS IGUAIS
#ESCALENO: TODOS OS LADOS DIFERENTES
print('VERIFICAÇÃO DE TRIÂNGULO')
m1 = str(input('Informe a primeira medida em centímeros: ')).strip()
m1 = float(m1)
m2 = str(input('Informe a segunda medida em centímetros: ')).strip()
m2 = int(m2)
m3 = str(input('Informe a terceira medida em centímetros: ')).strip()
m3 = int(m3)
if (abs(m1 - m2) < m3 < m1 + m2) and (abs(m1 - m3) < m2 < m1 + m3) and (abs(m2 - m3) < m1 < m2 + m3):
    if m1 == m2 == m3:
        print('É possível criar um triângulo do tipo EQUILÁTERO com estas medidas.')
    elif m1 == m2 != m3 or m1 == m3 != m2 or m2 == m3 != m1:
        print('É possível criar um triângulo do tipo ISOCELES com estas medidas.')
    elif m1 != m2 and m1 != m3 and m2 != m3:
        print('É possível criar um triângulo do tipo ESCALENO com estas medidas')
else:
    print('Não é possível criar um triângulo usando as medidas indicadas.')
