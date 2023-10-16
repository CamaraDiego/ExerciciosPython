#CRIAR UMA TUPLA ÚNICA COM NOMES E PREÇOS DE PRODUTOS
#EX: tupla = ('Pão', 2.50, 'Manteiga', 3.70, 'Leite', 1.80)
#NO FINAL MOSTRAR OS DADOS EM FORMA DE TABELA
tupla = ('Arroz', 12.50,
         'Feijao', 9.80,
         'Farofa', 4.20,
         'Tomate', 8.70,
         'Alface', 2.40,
         'Carne', 17.90,
         'Cerveja', 5.80,
         'Sorvete', 10.60,
         'Cobertura', 3.10)
print('=' * 38)
print(f'{"LISTA DE PRODUTOS E PREÇOS":^38}')
print('=' * 38)
for valor in tupla:
    if str(valor).isalpha():
        print('{:.<30}'.format(valor), end = '')
    elif str(valor).replace('.', '').isnumeric():
        print(f'R$ {float(valor):>5.2f}')
print('=' * 38)
