# Nota de aluno

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print(f'A média do aluno é {media}.')
if 7 > media >= 5:
    print('Média entre de 5.0 e 6.9, ALUNO EM RECUPERAÇÃO!')
elif media < 5:
    print('Média abaixo de 5.0, ALUNO REPROVADO!')
elif media >= 7:
    print('Média 7.0 ou superior, ALUNO APROVADO!')