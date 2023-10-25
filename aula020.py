def mostralinha():
    print('-=-' * 15)


mostralinha()
print(f'{"ÍNICIO DO PROGRAMA":^45}')
mostralinha()

def mensagem(msg):
    print('-=-' * 15)
    print(msg)
    print('-=-' * 15)


mensagem(f'{"ÍNICIO DO PROGRAMA":^45}')

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 1, 3)
contador(0, 2, 4, 5)
contador(1, 2)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1
    print(lst)


valores = [7, 2, 5, 0, 4]
dobra(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


soma(2, 5)
soma(2, 9, 4)
