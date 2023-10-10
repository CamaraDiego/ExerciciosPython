#PERGUNTAR O VALOR DE UMA CASA PARA EMPRESTIMO BANCARIO
#PERGUNTAR O SALARIO DO COMPRADOR
#PERGUNTAR EM QUANTOS ANOS SERA FEITO O PAGAMENTO
#CALCULAR O VALOR DA PRESTACAO MENSAL
#PRESTACAO NAO PODE EXCEDER 30% DO SALARIO OU O EMPRESTIMO É NEGADO

v = str(input('Informe o valor da casa para financiamento R$')).strip()
v = float(v)
s = str(input('Informe o salário do comprador R$')).strip()
s = float(s)
a = str(input('Em quantos anos pretende fazer o pagamento?\n')).strip()
a = int(a)
vp = v / (a * 12)
if vp <= s * 0.30:
    print("""Para financiamento de uma casa no valor de R${:.2f}
à ser pago em {} anos, o valor da prestação mensal
é de R${:.2f}.""".format(v, a, vp))
else:
    print("""Financiamento não pode ser efetivado, pois o valor
das parcelas para este financiamento que é de R${:.2f}
excede 30% do salário do comprador.""".format(vp))
