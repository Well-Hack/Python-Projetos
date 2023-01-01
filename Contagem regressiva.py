from time import sleep
print('='*100)
print('\33[32;33;31m CONTAGEM REGRESSIVA PARA O ANO NOVO \33[m')
print('='*100)
n = str(input("Pressione '1' para começar a contagem: "))
if n == '1':
        for c in range (10, 0, -1):
            print(c)
            sleep(1)
        print('FELIZ ANO NOVO!')
else:
    print('Tecla errada')