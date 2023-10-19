print('Exercicio 94 - Crie um programa que leia nome, sexo e idade de várias pessoas, \n'
      'guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:\n'
      'A) Quantas pessoas foram cadastradas \n'
      'B) A média de idade \n'
      'C) Uma lista com as mulheres \n'
      'D) Uma lista de pessoas com idade acima da média')
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apeans S ou N. ')
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas. ')
media = soma / len(galera)
print(f'A media de idade é de {media:5.1f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print('D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
        print()
print("ENCERRADO")