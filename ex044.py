#PEDIR O VALOR DE UM PRODUTO
#CALCULAR DESCONTO DE ACORDO COM O METODO DE PAGAMENTO
#A VISTA DINHEIRO/CHEQUE 10%
#A VISTA CARTAO 5%
#ATE 2X NO CARTAO PRECO NORMAL
#3X OU MAIS NO CARTAO 20% DE JUROS

preco = str(input('Informe o preço do produto R$')).strip()
preco = float(preco)
pag = str(input("""Informe o método de pagamento
1. À VISTA (DINHEIRO/CHEQUE)
2. À VISTA (CARTÃO)
3. ATÉ 2X (CARTÃO)
4. 3X OU MAIS (CARTÃO)\n""")).strip()
pag = int(pag)
if pag == 1:
    preco = preco * 0.90
    print('O preço final do produto é de R${:.2f}.'.format(preco))
elif pag == 2:
    preco = preco * 0.95
    print('O preço final do produto é de R${:.2f}.'.format(preco))
elif pag == 3:
    print('O preço final do produto é de R${:.2f}.'.format(preco))
elif pag == 4:
    preco = preco * 1.20
    print('O preço final do produto é de R${:.2f}.'.format(preco))
else:
    print('Opção de pagamento inválida.')
