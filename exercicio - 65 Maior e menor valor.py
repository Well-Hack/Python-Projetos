print('Exercicio - 65 Crie um programa que leia varios numeros inteiros pelo teclado e no final da execusão'
      ' mostre a media entre todos os valores e qual foi o maior e o menor valor lido. O programa ele deve'
      'perguntar ao usuario se ele quer ou não continaur a digitar valores')
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'sS':
    num = int(input('Digite um valor: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
    resp = str(input('Deseja Continuar? [S/N] ')).upper().strip()
media = soma / quant
print('O maior numero digitado foi {} e o menor foi {}'.format(maior,menor))
print('Voce digitou {} numeros e a media foi {}'.format(quant,media))
print('Acabou')
