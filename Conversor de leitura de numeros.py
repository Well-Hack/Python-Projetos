n = int(input('Por favor, digite um número: '))
es = int(input('\n [1] - Para binário,\n [2] - Para octadecimal,\n [3] - Para hexadecimal \n'))
if es == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif es == 2:
    print('{} convertido para Octal é igual a {}'.format(n, oct(n)[2:]))
elif es == 3:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, hex(n)[2:]))
