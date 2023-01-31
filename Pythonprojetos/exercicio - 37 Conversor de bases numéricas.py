print('Exercicio - 37 Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher '
      'qual será a \033[1;34m base de conversão \033[m')
print('***** \033[1;34m base de conversão \033[m *****')
N = int(input('Escreva um número qualquer: '))
C = int(input('Agora qual base de conversão voce deseja \033[1;34m 1 para Binario, 2 para octal e 3 para Hexadecimal: \033[m'))
if C == 1:
    print('O seu número {} em \033[1;34m BINARIO\033[m, fica {}'.format(N, bin(N)[2:]))
elif C == 2:
    print('O seu número {} em \033[1;34m OCTAL\033[m, fica {}'.format(N, oct(N)[2:]))
elif C == 3:
    print('O seu número {} em \033[1;34m HEXADECIMAL\033[m, fica {}'.format(N, hex(N)[2:]))
else:
    print('Opção INVALIDA')
