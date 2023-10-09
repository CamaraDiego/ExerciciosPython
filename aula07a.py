nome = str(input('Qual o seu nome? '))
ola = ('Olá')
bemvindo = ('Bem vindo')
print('='*20)   #vai imprimir 20 vezes o símbolo =
print('{:«<20}'.format(ola))        #vai apresentar em 20 caracteres alinhado à esquerda preenchendo os vazios com «
print('{:=^20}'.format(nome))       #vai apresentar em 20 caracteres alinhado ao centro preenchendo os vazios com =
print('{:»>20}'.format(bemvindo))   #vai apresentar em 20 caracteres alinhado à direita preenchendo os vazios com »
print('='*20)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
d = n1 / n2
print('A divisão de {:.2f} \n por {:.2f} \n é igual a {:.2f}.'.format(n1, n2, d), end = ' ')
print('Tenha um bom dia')
