#LER 3 NUMEROS
#DIZER QUAL É O MENOR
#DIZER QUAL É O MAIOR
print('Informe três números diferentes')
n1 = str(input('Digite um número:\n')).strip()
n1 = float(n1)
ma = me = n1
n2 = str(input('Digite outro número:\n')).strip()
n2 = float(n2)
if n2 > n1:
    ma = n2
elif n2 < n1:
    me = n2
n3 = str(input('Digite o último número:\n')).strip()
n3 = float(n3)
if n3 > ma:
    ma = n3
elif n3 < me:
    me = n3
print('O menor número digitado foi {:.2f}.'.format(me))
print('E o maior número digitado foi {:.2f}.'.format(ma))
