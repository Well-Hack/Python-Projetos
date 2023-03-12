print('Exercicio - 77 Crie um programa que tenha uma tupla com várias palavras \n'
      ' (não usar acentos). Depois disso, você deve mostrar, \n'
      'para cada palavra, quais são as suas vogais.')

print('=+'*20)
print('Contando vogais em Tuplas')
print('=+'*20)

frase = ('Maca', 'Caju', 'Banana', 'Tomate', 'Limao', 'Maracuja')
print(frase)

for p in frase:
    print(f' \nA palavra {p.upper()} tem as vogais', end=' ')
    for vogais in p:
        if vogais.lower() in 'aeiou':
            print(vogais, end=' ')

