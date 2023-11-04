try:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite o segundo numero: '))
    r1 = n1 / n2
except Exception as erro:
    print(f'Infelizmente tivemos problema, o erro encontrado foi {erro.__class__}')
else:
    print(f'Os numeros {n1} e {n2} dara o resultado: {r1:.2f}')
finally:
    print('Tudo certo')