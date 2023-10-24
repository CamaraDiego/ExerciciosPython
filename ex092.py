#LER NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO
#CADASTRAR COM A IDADE E NÃO COM O ANO DE NASCIMENTO
#CASO A CARTEIRA DE TRABALHO SEJA DIFERENTE DE ZERO
#TAMBÉM CADASTRAR ANO DE CONTRATAÇÃO E SALÁRIO
#CALCULAR COM QUANTOS ANOS A PESSOA VAI SER APOSENTAR (APÓS 35 ANOS DE CONTRIBUIÇÃO)

from datetime import date
from time import sleep
dicionario = dict()
dicionario['nome'] = str(input('Informe o nome: ')).strip()
nascimento = int(input('Ano de nascimento: '))
dicionario['idade'] = date.today().year - nascimento
dicionario['ctps'] = int(input('Carteira de Trabalho (0 caso não tenha): '))
if dicionario['ctps'] == 0:
    print('-=-' * 15)
    for k, v in dicionario.items():
        print(f' - {k} tem o valor {v}')
        sleep(0.5)
else:
    dicionario['contratacao'] = int(input('Ano de contratação: '))
    dicionario['salario'] = float(input('Salário: R$'))
    dicionario['aposentadoria'] = dicionario['contratacao'] - nascimento + 35
    print('-=-' * 15)
    for k, v in dicionario.items():
        print(f' - {k} tem o valor {v}')
        sleep(0.5)
