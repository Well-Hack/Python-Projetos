print('Exercicio - 83  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. \n'
      ' Seu aplicativo deverá analisar se a expressão passada está \n'
      'com os parênteses abertos e fechados na ordem correta.')

print('=+'*30)
print('Validando expressões matemáticas')
print('=+'*30)

expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            del pilha[-1]
        else:
            pilha.append=(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta valida')
else:
    print('Sua expressão esta errada')