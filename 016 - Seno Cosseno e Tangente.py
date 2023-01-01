import math
num = float(input('Digite um angulo: '))
s1 = math.sin(math.radians(num))
c1 = math.cos(math.radians(num))
t1 = math.tan(math.radians(num))
print('O seno {:.2f}'.format(s1))
print('O cosseno {:.2f}'.format(c1))
print('A tangente {:.2f}'.format(t1))