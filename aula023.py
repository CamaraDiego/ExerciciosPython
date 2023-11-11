try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Infelizmente tivemos um erro do tipo {erro.__class__}.')
except (ValueError):
    print('Houve um problema pelo tipo inserido.')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito obrigado!')
