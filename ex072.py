#CRIAR UMA TUPLA PREENCHIDA COM CONTAGEM POR EXTENSO DE 0 ATÉ 20
#LER UM NÚMERO ENTRE 0 E 20
#MOSTRAR ESTE NÚMERO POR EXTENSO
from time import sleep
tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
         'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
         'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
         'Desesseis', 'Desessete', 'Dezoito', 'Dezenove', 'Vinte')
print('-=-' * 13)
numero = str(input('Digite um número inteiro entre 0 e 20: ')).strip()
print('-=-' * 13)
while (numero.isnumeric() == False) or ((int(numero) < 0) or (int(numero) > 20)):
    numero = str(input('Digite um número inteiro entre 0 e 20: ')).strip()
    print('-=-' * 13)
numero = int(numero)
sleep(0.5)
print(f'Você digitou o número {tupla[numero]}')
