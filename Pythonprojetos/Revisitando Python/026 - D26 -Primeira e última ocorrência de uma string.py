print('Desafio 26 - Faça um programa que leia uma frase pelo teclado e mostre \n'
      'quantas vezes aparece a letra “A”, em que posição ela aparece a primeira \n vez e em'
      ' que posição ela aparece a última vez.')
print('=*' * 30)
print('Primeira e última ocorrência de uma string')
print('=*' * 30)
fr = str(input('Digite Algo: ')).upper()
total = fr.count('A')
po = fr.find('A')
pu = fr.rfind('A')
print(f'Tem {total} Letras A, a primeira ocorrencia ocorre em {po} e a ultima ocorrencia é {pu}')

