#PEDIR O NOME DE UAM CIDADE
#DIZER SE COMEÇA OU NÃO COM SANTO

cidade = str(input('Informe o nome da cidade:\n')).strip()
cidade = cidade.upper().split()
print('A cidade começa com Santo?')
if ('SANTO' in (cidade[0])) == True:
    print('Sim')
else:
    print('Não')
