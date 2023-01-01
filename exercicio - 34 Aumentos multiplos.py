print('Exercicio - 34 Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento'
      'para salarios superiores á R$1.250, calculeo aumento de 10% \n para inferiores ou iguais o aumento é de 15%')
sla = float(input('DIgite o valor de seu salário em reais R$: '))
if sla <= 1250:
    sln = sla*0.15 + sla
    print('Seu salário antigo era de {:.2f}, agora com aumento de 15%, seu novo salário é de: R${:.2f}'.format(sla,sln))
else:
    sln = sla * 0.10 + sla
    print('Seu salário antigo era de {:.2f}, agora com aumento de 10%, seu novo salário é de: R${:.2f}'.format(sla, sln))
