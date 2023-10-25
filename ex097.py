#UMA FUNÇÃO CHAMADA ESCREVA
#USUARIO DIGITAR QUALQUER TEXTO COM QUALQUER TAMANHO
#MOSTRAR A MENSAGEM FINAL COM AS BARRAS SUPERIOR E INFERIOR ADAPTÁVEL AO TAMANHO DO TEXTO

def escreva(txt):
    comprimento = int(len(txt) + 4)
    print('-' * comprimento)
    print(f'{txt:^{comprimento}}')
    print('-' * comprimento)


txt = str(input('Digite um título:\n'))
escreva(txt)
