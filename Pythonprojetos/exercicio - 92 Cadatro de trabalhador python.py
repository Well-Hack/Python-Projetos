print('Exercicio 92 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o \n'
      '(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também \n'
      ' o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.')
from datetime import datetime
cadastro = {}
print("=+"*30)
print("Cadastro de funcionário")
print("=+"*30)

print("Bem vindo ao cadastramento de funcionario! \n")
cadastro['nome'] = str(input('Por Favor, digite o nome do funcionário: '))
cadastro['nascimento'] = int(input(f'Por Favor, digite o ano de nascimento do {cadastro["nome"]}: '))
cadastro['idade'] = datetime.now().year - cadastro['nascimento']
cadastro['ctps'] = int(input(f'Digite a CTPS de {cadastro["nome"]} caso não tenha, digite 0: '))
if cadastro['ctps'] != 0:
    cadastro['contrato'] = int(input(f'Digite o ano de contratação: '))
    cadastro['salário'] = int(input('Digite o salário: '))
    cadastro['aposentadoria'] = 35 - (datetime.now().year - cadastro['contrato'])
    print(f'=='*10)
    print(f'Segue os dados... \n'
          f'O nome do funcionário é {cadastro["nome"]} \n'
          f'Ele tem {cadastro["idade"]} anos \n'
          f'Ele tem como Carteira de trabalho a numeração {cadastro["ctps"]}\n'
          f'Ele se aposentará daqui há {cadastro["aposentadoria"]} anos')
else:
    print(f'=='*10)
    print(f'Segue os dados... \n'
          f'O nome do funcionário é {cadastro["nome"]}\n'
          f'Ele tem {cadastro["idade"]} anos \n'
          f'E não tem Carteira de trabalho')


