print('Exercicio - 54 Faça um programa que leia o ano de nascimento de sete pessoa. No final, mostre quantas pessoas \n'
      'ainda não atingiram a maioridade e quantas já são maiores')
from datetime import date
print('*-'*30)
print('\033[1:34m Grupo da maioridade Penal \033[m')
print('*-'*30)
atual = date.today().year
tmaior = 0
tmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        tmaior += 1
    else:
        tmenor += 1
print('Temos {} pessoas que são menor de idade. '.format(tmenor))
print('Existem {} pessoas que são maiores de idade.'.format(tmaior))