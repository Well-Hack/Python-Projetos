print('Faça um programa que mostre a tabuada de varios numeros, um de cada vez para cada valor digitado pelo \n'
      'usuario. O programa será interrompido quando o numero solicitado'
      ' for negativo')
u1 = 0
while True:
    u1 = int(input('Quer ver tabuada de qual valor? '))
    if u1 < 0:
        break
    print('--'*30)
    for c in range (1,11):
        res = c * u1
        print(f'{u1} x {c} = {res}')
    print('--'*30)
print('--' * 30)
print('Programa encerrado, Até a próxima')
print('--'*30)