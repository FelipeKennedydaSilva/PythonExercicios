al = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(al))
print('Só tem espaço? ', al.isspace())
print('É um número? ', al.isnumeric())
print('É alfabético? ', al.isalpha())
print('É alfanumérico? ', al.isalnum())
print('Está em maiúsculas? ', al.isupper())
print('Está em minusculas? ', al.islower())
print('Está capitalizada? ', al.istitle())