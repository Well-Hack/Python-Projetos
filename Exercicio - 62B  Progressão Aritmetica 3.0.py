print('Refaça progressão aritimetica V3.0')
print('Gerador de PA')
print('-='*20)
p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
t = p
c = 1
total = 0
m = 10
while m != 0:
    total += m
    while c <= total:
        print('{} > '.format(t), end='')
        t += r
        c += 1
    print('Pausa')
    m = int(input('Quantos termos voce quer colocar a mais? '))
print('Progresão finalizada com {} termos mostrados.'.format(total))
print('FIM')