print('Exercicio - 43 desenvolva uma lógica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status \n'
      '. de acordo com a tabela abaixo. \n'
      '- Abaixo do 18.5: ABAIXO DO PESO \n'
      '- Entre 18.5 e 25: PESO IDEAL \n'
      '- Entre 25 e 30: SOBREPESO \n'
      '- Entre 30 e 40: OBESIDADE \n'
      '- Acima de 40: OBESIDADE MORBIDA \n')
print('+++'*30)
print('INDICE DE MASSA CORPORAL')
print('+++'*30)
a = float(input('Por gentileza, informe a sua altura: '))
p = float(input('Por gentileza, informe o seu peso: '))
imc = p / (a * a)
if imc < 18.5:
    print('Você está ABAIXO DO PESO, seu IMC é {:.2f}'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Você está no peso IDEAL, seu IMC é {:.2f}'.format(imc))
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO, seu IMC é {:.2f}'.format(imc))
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE, seu IMC é {:.2f}'.format(imc))
else:
    print('Você está com OBESIDADE MORBIDA, seu IMC é {:.2f}'.format(imc))