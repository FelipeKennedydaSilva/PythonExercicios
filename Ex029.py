# Radar de velocidade, verificando e aplicando a multa!
velocidade = int(input('Qual é a velocidade atual do carro? '))
x = (velocidade - 80)*7
if velocidade > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h \nVocê deve pagar uma multa de RS{x:.2f}')
print('Tenha um bom dia! \nDirija com segurança!')