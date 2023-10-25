print ('Exercício 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante \n'
',a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. \n'
'Ex: n = leiaInt(Digite um n: )')

def LeiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m Erro! Digite um numero valido \033[m')
        if ok:
            break
    return valor


n = LeiaInt("Digite um numero: ")
print(f'O numero que você digitou foi: {n}')
