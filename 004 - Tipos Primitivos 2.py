var = (input('Digite algo: '))
print('O tipo primitivo desse valor é',type(var))
print('Só tem espaço?',var.isspace())
print('É um numero? ',var.isnumeric())
print('É alfabético?',var.isalpha())
print('É alfanumérico?',var.isalnum())
print('Está em maiuscula?',var.isupper())
print('Está em minuscula?',var.islower())
print('Está capitalizada?',var.istitle())