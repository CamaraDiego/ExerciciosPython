lista = [n1, n2, n3, n4]

for c in lista:
    print(f'O item selecionado é {c}.') #mostra somente o valor inserido

for cont1 in range(0, len(lista)):
   print(f'na posição {cont1} está contido o valor {lista[cont1]}.')   #mostra a posição e o valor inserido

for cont2, item in enumerate(lista):
    print(f'na posição {cont2} está contido o valor {item}.')   #mostra a posição e o valor inserido, primeira variavel do for referente à posição e segunda referente ao conteúdo
==================================================================================
tupla = (1, 2, 3, 4, 5, 3,)
print(tupla.index(3, 3))
==================================================================================
pessoa = ('Diego', 34, 'M', 76.50) #a tupla pdoe conter elementos com tipo primitivo diferentes
==================================================================================
del(pessoa) #deleta a tupla inteira
