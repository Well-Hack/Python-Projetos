print('Desafio 3 - Faça um programa que leia algo pelo  \n'
      'teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.')

print('=*'*30)
print('Dissecando Variavel')
print('=*'*30)

a1 = input('Digite algo: ')
print('É alfabetica? ',a1.isalpha())
print('é numerico? ',a1.isnumeric())
print('É maiuscula? ',a1.isupper())
print('É minuscula? ',a1.islower())
print('é alfanumerica?',a1.isalnum())
print('Ó tipo primitico desse valor é?',type(a1))