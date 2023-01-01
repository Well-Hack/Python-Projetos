print('Exercicio - 62 Refaça o DESAFIO 61. Lendo o primeiro termo e a razão de uma PA. MOstrando os 10 primeiros '
      'termos da progressão usando a estrutura while. Perguntando ao usuario se ele quer mostrar mais algum termo ')
print('#'*30)
print('\033[1:32m PROGRESSÃO ARITIMETICA VERSÃO 3.0\033[m')
print('#'*30)
pt = 1
r = int(input('Digite a razão que será usada!: '))
while pt != 0:
    soma = 0
    pt = int(input('Digite o Primeiro Termo, caso queira sair é só digitar [0]: '))
    while soma != 10 and pt != 0:
        soma += 1
        print('{}  '.format(pt), end='')
        pt += r
    print('\n')
print('ACABOU')