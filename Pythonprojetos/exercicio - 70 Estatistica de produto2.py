print('Exercicio - 70 Crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar'
      'se o usuário vai continuar. No Final. MOstre...'
      '[A] Qual é o total de gastos na compra.'
      '[B] QUantos produtos custam mais de 1000 reais.'
      '[C] Qual é o nome do produto mais barato. ')
q1 = 'S'
total = 0
m10 = 0
barato = ' '
real = 0
cont = 0
menor = 0
while q1 == 'S':
        produto = str(input('Qual o nome do produto? '))
        real = float(input('Qual valor do produto em R$: '))
        cont += 1
        total += real
        if real >= 1000:
            m10 += 1
        if cont == 1:
            barato = produto
        else:
            if real < menor:
                menor = real
                barato = produto
        q1 = str(input('Deseja cadastra mais algum produto? [S/N]: ')).upper().strip()[0]
        if q1 == 'N':
            print(f'Os dados coletatos totais foram... ')
            print(f'O total de gastos foi de {total}')
            print(f'A quantidade de produtos acima de R$1.000 foi de {m10} produtos')
            print(f'O produto mais barato foi o/a {barato}')
            break