print('Exercicio 57 -  Faça um programa que leia o sexo de uma pessoa. mas só aceite valores "M" ou "F".\n'
      'Caso esteja errado, peça a digitação novamente até ter um valor correto.')
print('*'*50)
print('\033[032:1m VALIDADOR DE GENERO \033[m')
print('*'*50)
nome = str(input('Ola! Bem vindo!, Informe Por gentileza o seu nome completo: '))
i = int(input('Ok \033[032:1m {} \033[m , agora vou pedir que voce digite a sua idade: '.format(nome)))
s = str(input('Certo \033[032:1m {} \033[m, agora vou pedir que voce me informe o seu sexo, M para masculino ou F para Feminino: '.format(nome))).strip().upper()[0]
while s != 'M' and 'F':
    print('Desculpe, digito invalido, tente novamente.')
    s = str(input('M para masculino ou F para Feminino: ')).upper
cid = str(input('Muito bem, agora me diga a sua cidade: '))
