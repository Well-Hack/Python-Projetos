print('Exercicio 96 - Faça um programa que tenha uma'
      'função chamada escreva(), que recebe um texto'
      'qualquer como ṕarametro e mostre uma mensagem'
      'com tamanho adaptável')


def escreva(msg):
    print('='*len(msg))
    print(msg)
    print('='*len(msg))


escreva('Curso em Video na hora')