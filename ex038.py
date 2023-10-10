#LER DOIS NUMEROS INTEIROS
#COMPARAR
#O PRIMEIRO NUMERO E MAIOR
#O SEGUNDO VALOR E MAIOR
#NAO EXISTE VALOR MAIOR OS DOIS SAO IGUAIS
maior = 0
n1 = str(input('Informe um número inteiro: ')).strip()
n1 = int(n1)
maior = n1
n2 = str(input('Informe mais um número inteiro: ')).strip()
n2 = int(n2)
if n2 > maior:
    maior = n2
    print('O segundo número digitado {} é o maior.'.format(maior))
elif n1 == maior and n1 != n2:
    print('O primeiro número digitado {} é o maior'.format(maior))
elif n1 == n2:
    print('Não existe número maior, ambos são iguais {}.'.format(n1))
