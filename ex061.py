#LER O PRIMEIRO TERMO E A RAZAO DE UMA PA USANDO O WHILE
#MOSTRAR OS 10 PRIMEIROS TERMOS
from time import sleep
termo = str(input('Informe o primeiro termo: ')).strip()
while (termo.isnumeric() == False) and (termo.replace('.', '').isnumeric() == False):
    termo = str(input('Valor inválido, informe um número para o primeiro termo: '))
termo = float(termo)
razao = str(input('Informe a razão: ')).strip()
while (razao.isnumeric() == False) and (razao.replace('.', '').isnumeric() == False):
    razao = str(input('Valor inválido, informe um número para a razão: '))
razao = float(razao)
c = 1
prog = 0
print('=' * 18)
print('{}º termo = {:.2f}'.format(' 1', termo))
while c < 10:
    prog = termo + razao * c
    sleep(0.5)
    print('{:2}º termo = {:.2f}'.format(c + 1, prog))
    c = c + 1
sleep(0.5)
print('=' * 18)
print('{:^18}'.format('FIM'))
print('=' * 18)
