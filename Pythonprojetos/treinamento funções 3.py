def contador(*num):
    for valor in num:
        print(valor, end=' ')
        tam = len(num)
    print(f'Recebi {tam} numeros')
    print('FIM')



contador(2,1,7)
contador(4,8,9,1,6)
contador(7,2,3,9)