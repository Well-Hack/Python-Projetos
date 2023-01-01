nome = str(input('Digite o nome do funcionário que receberá o aumento: '))
sal = float(input('Informe o valor do salário que ele recebe atualmente em R$: '))
if sal <= 1250.00:
    nsal = sal + (sal * 15 / 100)
    print('O funcionário {} teve 15% de aumento e que gerará um salário novo de R${:.2f}'.format(nome,nsal))
else:
    nsal = sal + (sal * 10 / 100)
    print('O funcionário {} teve 10% de aumento e que gerará um salário novo de R${:.2f}'.format(nome,nsal))