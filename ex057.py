#LER O SEXO DE UMA PESSOA
#SO ACEITE 'M' OU 'F'
#CASO ERRADO PEDIR PRA DIGITAR NOVAMENTE ATÉ TER UM VALOR CORRETO

sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()
while (sexo in 'MF') == False:
    sexo = str(input('Informação inválida, informe seu sexo [M/F]: ')).upper().strip()
print('Obrigado.')
