#UM MINI SISTEMA QUE FUNCIONA COM O INTERACTIVE HELP DO PYTHON
#O USUÁRIO VAI DIGITAR UM COMANDO E VAI APARECER SEU MANUAL
#TERMINAR SÓ QUANDO O USUÁRIO DIGITAR FIM

def ajuda(com):
    while True:
        if com.upper() == 'FIM':
            break
        help(com)
        com = str(input('Digite a função para seu manual ou FIM para terminar: ')).strip()


funcao = ajuda(str(input('Digite a função para seu manual ou FIM para terminar: ')))
