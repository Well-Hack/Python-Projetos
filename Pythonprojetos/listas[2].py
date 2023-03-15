completo = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Digite o seu nome: ')))
    dado.append(int(input('Digite a sua idade: ')))
    completo.append(dado[:])
    dado.clear()

for p in completo:
    if p[1] > 21:
        print(f'A pessoa {p[0]} tem {p[1]} anos de idade')
