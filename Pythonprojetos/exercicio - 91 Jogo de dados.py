print("Exercicio - 91 Crie um Crie um programa onde 4 jogadores joguem um dado e tenham \n "
      "resultados aleatórios. Guarde esses resultados em um dicionário em \n"
      " Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou"
      "\n o maior número no dado.")
from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
 print(f'{k} tirou {v} no dado.')
 sleep(2)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate (ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} ')
    sleep(1)