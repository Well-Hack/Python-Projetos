print(' Exercicio - 36 Escreva um programa para aprovar emprestimo bancário para compra de uma casa \n'
      ' O programa vai perguntar o \033[1;31m valor \033[m  da casa, o \033[1;31m salário \033[m do comprador e em \033[1;31m quantos anos \033[m ele vai pagar \n'
      ' Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% \n'
      ' do salário ou entao o empréstimo será negado')
print('=^'*50)
print('\033[1;32m Aprovação de Emprestimo \033[m')
print('=^'*50)
nome = str(input('Qual seu nome? '))
vlr = float(input('É um prazer {}. Por gentileza, digite o \033[1;33m valor \033[m que voce deseja: '.format(nome)))
slr = float(input('Agora digite o seu \033[1;33m salário \033[m: '))
anos = int(input('Em quantos anos você deseja pagar o emprestimo? '))
meses = anos * 12
vlr2 = vlr / meses
if vlr2 <= (0.30 * slr):
    print('Empréstimo \033[1;32m Aprovado \033[m \nVoce terá {} meses para pagar o empréstimo e cada mensalidade ficará no valor de {:.2f}'.format(meses, vlr2))
else:
    print('Emprestimo \033[1;31m negado \033[m , ultrapassou 30% do seu salário')
