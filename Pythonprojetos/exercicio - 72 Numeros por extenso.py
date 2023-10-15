print('Exercicio 72 - Escreva um programa que tenha uma tupla totalmente preenchida por extenso com uma contagem \n'
      'de zero até vinte. Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostra-lo por extenso')
n1 = ('Zero', 'Um', "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Cartoze", "Quinze", "Dezesseis", "Dezesete", "Dezoito", "Dezenove", "Vinte")
print("="*20)
print('Numeros por Extenso')
print("="*20)

while True:
      n2 = int(input("Por favor Digite um numero de 0 a 20: "))
      if 0 <= n2 <= 20:
            break
      print('Tente Novamente. \n', end=" ")
print(f"Você digitou o numero {n1[n2]}")

