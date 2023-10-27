#FUNÇÃO CHAMADA VOTO
#RECEBE ANO DE NASCIMENTO DE UMA PESSOA (INFORMADO PELO USUARIO E CALCULAR A IDADE)
#NO FINAL INDICAR SE PDOE VOTAR, SE É OPCIONAL OU SE É OBRIGATÓRIO
def voto(p):
    from datetime import date
    idade = date.today().year - p
    if idade < 16:
        return (f'Com {idade} anos, não pode votar.')
    elif 16 <= idade < 18 or 65 < idade:
        return (f'Com {idade} anos, o voto é opcional.')
    elif 18 <= idade < 65:
        return (f'Com {idade} anos, o voto obrigatório.')


nasc = int(input('Informe o ano de nascimento: '))
print(voto(nasc))
