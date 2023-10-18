#USUARIO INSERIR 5 VALORES NUMÉRICOS
#CADASTRAR OS VALORES EM UMA LISTA JÁ NA POSIÇÃO CORRETA EM ORDEM CRESCENTE (SEM USAR O SORT)
#MOSTRAR A LISTA NO FINAL
lista = [0]
for c in range(0, 5):
    valor = str(input('Insira um valor: ')).strip()
    while valor.isnumeric() == False:
        valor = str(input('Valor inválido, digite um valor inteiro: ')).strip()
    valor = int(valor)
    while True:
        for pos, dado in enumerate(lista):
            if valor == 0:
                lista.insert(0, valor)
                break
            if (valor != 0) and (valor < dado):
                lista.insert(pos, valor)
                break
            if (valor != 0) and (valor > max(lista)):
                lista.append(valor)
                break
        break
del lista[0]
print('A lista de números digitados em ordem crescente é:')
print(lista)
