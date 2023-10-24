dados = {'nome':'Maria', 'idade':45}
dados['sexo'] = 'F'
pessoas = list()
for k, v in dados.items():
    print(f'O {k} é {v}')
