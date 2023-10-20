def calculo(a, b):
    s = a * b
    print('='*30)
    print(f'A area {a} metros de altura x por {b} metros de comprimento, é de: {s}')
    print('=' * 30)


print('='*20)
print('Calculo de área')
print('='*20)

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

calculo(a,b)