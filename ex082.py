#LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA, PERGUNTAR SE QUER CONTINUAR
#CRIAR DUAS LISTAS EXTRAS
#UMA SOMENTE COM NUMEROS PARES
#OUTRA SOMENTE COM NUMEROS IMPARES
#MOSTRAR AO FINAL AS TRES LISTAS GERADAS
lista = list()
while True:
    valor = str(input('Digite um valor inteiro: ')).strip()
    while valor.isnumeric() == False:
        valor = str(input('Valor inválido, digite um valor inteiro: ')).strip()
    valor = int(valor)
    lista.append(valor)
    cont = str(input('Quer continuar? [S/N]: ')).upper()
    while (cont.isalpha() == False) or ((cont in 'SN') == False):
        cont = str(input('Dado inválido, quer continuar? [S/N]: ')).upper()
    if cont == 'N':
        break
listapar = list()
listaimpar = list()
for dado in lista:
    if (dado % 2 == 0) and (dado != 0):
        listapar.append(dado)
    if dado % 2 != 0:
        listaimpar.append(dado)
print(f'A lista digitada é:\n{lista}')
print(f'Os números pares nesta lista são:\n{listapar}')
print(f'Os números ímpares nesta lista são:\n{listaimpar}')
