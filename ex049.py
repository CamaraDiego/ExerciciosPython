#FAZER A TABUADA DO NÚMERO QUE O USUARIO INFORMAR

num = str(input('Informe o número que deseja saber a tabuada:\n')).strip()
num = int(num)
for c in range(1, 11):
    print('{:2} x {:2} = {:2}'.format(num, c, num * c))
