#var.append() ADICIONA elementos na lista
#var.insert(n,'') INSERE elementos em uma lista em uma posição descrita
#del var[] Realiza deleção de um elemento em uma lista
#var.sort() Realiza a ordenação dos elementos
#var.sort(reverse=True)

num = [2,5,9,1]
print(num)
num.insert(2, 22)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
del num[2]
print(num)

for c, n in enumerate(num):
    print(f'Na posição {c} encontrei o valor {n}')
print('Pronto!')