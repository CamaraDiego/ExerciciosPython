nome = 'José'
idade = 33
salario = 1350.50
print(f'O {nome} tem {idade:2} anos e ganha R${salario:.2f}')

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma dos números digitados vale {s}.')
