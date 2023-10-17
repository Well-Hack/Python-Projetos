pessoas = {'nome':'Wellerson', 'idade':27, 'genero':'Masculino'}
del pessoas['genero']
for k, v in pessoas.items():
    print(f'{k} == {v}')