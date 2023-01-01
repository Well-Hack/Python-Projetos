from time import sleep
print('='*100)
print('\33[32;33;31m APENAS NUMEROS PARES \33[m')
print('='*100)
n = str(input("Pressione '1' para começar a contagem: "))
if n == '1':
    for c in range (0, 50, 2):
        print(c)
        sleep(1)
    print('Acabou')
else:
    print('Tecla errada')
