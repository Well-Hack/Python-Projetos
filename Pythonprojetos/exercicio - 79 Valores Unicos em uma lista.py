print('Exercicio - 79 Crie um programa onde o usuário possa digitar vários \n'
      ' valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, \n '
      'ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, \n'
      ' em ordem crescente.')

print('=+'*30)
print('Valores unicos em uma lista')
print('=+'*30)

n = list()
while True:
      n1 = int(input(f'Digite um valor: '))
      if n1 not in n:
            n.append(n1)
            print('Valor Adicionado com Sucesso!')
      else:
            print('Valor duplicado: Não vou adicionar')
      r = str(input('Quer Continuar? [S/N]: ')).upper()
      if r == 'N':
            break
n.sort()
print(f'O valores digitados foram: {n}')