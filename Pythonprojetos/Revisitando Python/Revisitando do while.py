
n1 = int(input('Digite um numero: '))
c = 1
while True:
    r = c * n1
    print(f'{n1} x {c} = {r}')
    c += 1
    if c >= 16:
        break
print('Obrigado')