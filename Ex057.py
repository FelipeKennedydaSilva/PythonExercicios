sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MnFf':
    sexo = str(input('Dados inválidos. Por favor, infome seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
