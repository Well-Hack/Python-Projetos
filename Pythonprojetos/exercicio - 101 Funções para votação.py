print('Exercicio 101 - Crie um programa que tenha \n'
      'uma função chamado voto() que vai receber como \n'
      'parametro o ano de nascimento de uma pessoa\nretornando'
      'um valor literal indicando se uma pessoa tem voto \n'
      'negado, opcional ou obrigatório nas eleições')

def voto():
      v = 'Voto é OBRIGATORIO'
      o = 'Voto é OPCIONAL'
      n = 'NÃO VOTA'
      if i >= 18:
            return print(v)
      elif i >= 16 <= 18:
            return print(o)
      else:
            return print(n)

i = int(input(f'Digite a sua idade: '))
print(f'você tem {i} anos de idade o seu ', end='')
voto()
