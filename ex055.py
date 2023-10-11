#LER O PESO DE 5 PESSOAS
#NO FINAL MOSTRAR QUAL O MAIOR E QUAL O MENOR
maior = menor = 0
for c in range(1, 6):
    peso = str(input('Informe o peso (em Kg) da {}ª pessoa: '.format(c))).strip()
    peso = float(peso)
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('Neste grupo de pessoas o menor peso registrado foi {:.2f}Kg.'.format(menor))
print('E o maior peso registrado foi {:.2f}Kg.'.format(maior))
