from datetime import date
nome = str(input('Hora da verdade. Fala seu nome ai: '))
nasc = float(input('Digite o ano que você nasceu: '))
ano = date.today().year
idade = ano - nasc
sn = str(input('Você tem \33[1;33m {:.0f}\33[m anos de idade, correto?'.format(idade)))
if sn.lower() == 'sim':
    peso = float(input('Digite agora o seu peso: '))
    alt = float(input('Agora digite a sua altura: '))
    print('Aguarde um momento enquanto realizamos os calculos...')
else:
    print('Então faça novamente:')
imc = peso / (alt * alt)
if imc < 18.5:
    print('Você está abaixo do peso {}, precisa comer muita pizza. Seu IMC foi de \33[1;32m {:.2f}\33[m'.format(nome, imc))
elif imc >= 18.5 and imc < 25.0:
    print('Você está no peso ideal {}, parabéns! Seu IMC foi de \33[1;32m {:.2f}\33[m'.format(nome, imc))
elif imc >= 25.0 and imc < 30.0:
    print('Você está gordo {}, precisa parar de comer. Seu IMC foi de \33[1;32m {:.2f}\33[m'.format(nome, imc))
elif imc >= 30.0 and imc < 40.0:
    print('Vocẽ é um gordão {}, vai acabar aumentando a fome do mundo. Seu IMC foi de \33[1;32m {:.2f}\33[m'.format(nome, imc))
elif imc >= 40.0:
    print('Você é um boomer {}, vai acabar morrendo. Seu IMC foi de \33[1;32m {:.2f}\33[m'.format(nome, imc))