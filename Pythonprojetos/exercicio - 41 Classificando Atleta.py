print('Exercicio - 41 A COnfederação Nacional de Natação precisa de um programa que leia o ano de nascimento de \n'
      'um atleta e mostre sua categoria de acordo com a idade \n'
      'ATE 9 ANOS: MIRIM \n'
      'ATÉ 14 ANOS: INFANTIL \n'
      'ATÉ 19 ANOS: JÚNIOR \n'
      'ATÉ 20 ANOS: SÊNIOR \n'
      'ACIMA DE 21 ANOS: MASTER')
print('^^'*30)
print('\033[1:34m TORNEIO DE NATAÇÃO \033[m')
print('^^'*30)
nome = str(input('Por favor, digite o nome do competidor: '))
id = int(input('Agora digite a idade de {}:'.format(nome)))

if id <= 9:
    print('O {} tem {} anos e competirá no torneio MIRIM'.format(nome,id))
elif id > 10 and id <= 14:
    print('O {} tem {} anos e competirá no torneio INFANTIL'.format(nome,id))
elif id > 14 and id <= 19:
    print('O {} tem {} anos e competirá no torneio JÚNIOR'.format(nome, id))
elif id > 19 and id <= 20:
    print('O {} tem {} anos e competirá no torneio SÊNIOR'.format(nome, id))
else:
    print('O {} tem {} anos e competirá no torneio MASTER'.format(nome, id))