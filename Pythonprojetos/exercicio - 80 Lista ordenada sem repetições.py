print('Exercicio - 80 Crie um programa onde o usuário possa digitar cinco valores numéricos e \n'
      'cadastre-os em uma lista, já na posição correta de inserção \n'
      ' (sem usar o sort()). No final, mostre a lista ordenada na tela..')

print('=+'*30)
print('Lista ordenada sem repetições')
print('=+'*30)

list = []
for c in range(5):
      n = int(input('Digite um valor: '))
      if c == 0 or n > list[-1]:
            list.append(n)
      else:
            pos = 0
            while pos < len(list):
                  if n <= list[pos]:
                        list.insert(pos,n)
                        break
                  pos += 1
print(f'Os valores digitados na lista em ordem foi{list}')