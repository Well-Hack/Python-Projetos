print('Exercicio - 73 Crie uma tupla preenchida com os 20 primeiros \n'
      'colocados da Tabela do Campeonato Brasileiro de Futebol, \n'
      'na ordem de colocação. Depois mostre:')

equipes =('Red Bull Racing', 'Aston Martin', 'Mercedes F1 Team', 'Scuderia Ferrari', 'Alfa Romeo', 'Alpine F1 Team', 'Williams Racing',
        'Scuderia Alpha Tauri', 'Haas F1 Team', 'Mclaren Racing')



print('=+'*30)
print('Informação da Formula 1')
print('=+'*30)

print('Escolha uma das opções a baixo: \n'
      '[1] Para ver os Três primeiros colocados \n'
      '[2] Para ver os Três Ultimos colocados \n'
      '[3] Em ordem Alfabética. \n'
      '[4] Buscar A Alfa Romeo na Classificação \n'
      'Ou qualquer outro opção para Encerrar o Programa \n')
while True:
    opcao = int(input('Qual você escolhe: '))
    if opcao == 1:
     print(equipes[:3])
    elif opcao == 2:
        print(equipes[7:])
    elif opcao == 3:
        print(sorted(equipes))
    elif opcao == 4:
        print(equipes.index('Alfa Romeo')+1)
    else:
        break
print('Obrigado')


