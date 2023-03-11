c = 1
n1 = 0
s = 0
while True:
    n1 = int(input(f'Digite o {c}º Numero: '))
    s += n1
    c += 1
    if c >= 5:
        break
print(f'A soma total é {s}')