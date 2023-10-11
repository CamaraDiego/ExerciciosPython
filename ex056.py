#LER NOME IDADE E SEXO DE 4 PESSOAS
#MOSTRAR NO FINAL
#MEDIA DE IDADE DO GRUPO
#NOME DO HOMEM MAIS VELHO
#QUANTAS MULHERES TEM MENOS DE 20 ANOS

soma = maior = menos = 0
velho = ''
for c in range(1, 5):
    print('{}ª PESSOA'.format(c))
    nome = str(input('Informe o nome: '.format(c))).strip()
    idade = str(input('Informe a idade: '.format(c))).strip()
    idade = int(idade)
    sexo = str(input('Informe o sexo [M/F]: '.format(c))).strip().upper()
    soma = soma + idade
    if 'M' in sexo and idade > maior:
        maior = idade
        velho = nome
    if 'F' in sexo and idade < 20:
        menos = menos + 1
print('=' * 20)
print('A média de idade neste grupo é de {:.2f} anos.'.format(soma/4))
print('O homem mais velho deste grupo é o {}, com {} anos.'.format(velho, maior))
print('A quantidade de mulheres com menos de 20 anos neste grupo é de {}.'.format(menos))
