# Criando uma analisador de credito
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
tempo = float(input('Quantos anos de financiamento? '))
prestacao = casa / (tempo * 12)
valor = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {tempo} anos a prestação será de R${prestacao:.2f} por mês.')
if prestacao <= valor:
    print('Empréstimo pode ser Concedido!')
else:
    print('Empréstimo Negado!')