print('Exercicio - 69 Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada '
      '\n o programa deverá perguntar se o usuario quer continaur ou não. No final, mostre:'
      '[A] Quantas pessoas tem mais de 18 anos; '
      '[B] Quantos homens foram cadastrados; '
      '[C] Quantas mulheres tem menos de 20 anos')
print('-='*30)
print('\033[032:1m REGISTRO GERAL \033[m')
print('-='*30)
maior = 0
h = 0
mm20 = 0
q1 = str(input('Você deseja cadastrar uma pessoa? ')).upper().strip()
if q1 == 'SIM':
    while True:
        idade = int(input('Qual a idade da pessoa? '))
        if idade >= 18:
            maior += 1
        sexo = str(input('E qual o sexo dela? [M] Masculino ou [F] Feminino? ')).upper().strip()
        if sexo == 'M':
            h += 1
        if idade <= 20 and sexo == 'F':
            mm20 += 1
        q1 = str(input('Deseja Continuar? ')).upper().strip()
        if q1 == 'NAO':
            print(f'Existem \033[1:32m {maior} \033[m pessoas acima de 18 anos;')
            print(f'Existem \033[1:32m {h} \033[m pessoas do sexo Masculino;')
            print(f'Existem \033[1:32m {mm20} \033[m Mulheres com menos de 20 anos')
            break
else:
    print('Então ate mais tarde ')