#USUARIO DIGITA UMA EXPRESSAO QUALQUER QUE USE PARENTESES
#ANALISAR SE A EXPRESSÃO PASSADA ESTA COM OS PARENTESES ABERTOS E FECHADOS DE FORMA CORRETA
#EX: ((a+b) + 3) == CORRETO
#    ((a+b) +3 == INCORRETO
expressao = str(input('Insira uma expressão qualquer: ')).strip()
lista = expressao.replace(' ', '').split()
if (lista[0].count('(')) != (lista[0].count(')')):
    print('Sua expressão está incorreta.')
else:
    print('Sua expressão está correta!')
