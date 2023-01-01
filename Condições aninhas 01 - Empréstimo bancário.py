nome = str(input('Olá, Bem-vindo ao empréstimo Nubank. Por favor, me informe o seu nome: ' ))
resp = (input('Certo \33[1;34m {}\33[m. Agora irei fazer algumas perguntas sobre as suas condições financeiras ok? '.format(nome)))
resp = resp.lower()
if resp == 'sim':
      casa = float(input('Qual o valor da casa em R$ que deseja comprar: '))
      sal = float(input('Agora, digite o valor em R$ do seu salário que recebe mensalmente: '))
      anos = float(input('Em quantos anos você pretende quitar essa divida? '))
      meses = anos * 12
      print('Transformando em meses ficaria em\33[1;32m {}\33[m vezes'.format(int(meses)))
      calc = casa / meses
      print('Cada parcela ficaria em R$\33[1;32m{:.2f}\33[m'.format(float(calc)))
if calc <= sal*30/100:
        print('Empréstimo \33[1;32m APROVADO {} \33[m. Estará disponivel em seu banco em 3 dias uteis'.format(nome))
elif calc > sal*30/100:
        print('Empréstimo\33[1;31m NEGADO\33[m Sinto muito, Obrigado!')
else:
    print('Infelizmente não podemos continuar sem a sua permissão. Obrigado!')
