print('Exercicio - 85  Crie um programa que declare uma matriz de \n'
      'dimensão 3×3 e preencha com valores lidos pelo teclado. \n'
      'No final, mostre a matriz na tela, com a formatação correta. ')

print('=+'*30)
print('Matriz em Python')
print('=+'*30)


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))
print("="*40)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print()


