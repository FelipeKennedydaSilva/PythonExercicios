# criando opções de pagamentos
print('Loja de Produtos')
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista dinheiro / pix;
[ 2 ] à vista cartão debito;
[ 3 ] 2x no cartão;
[ 4 ] 3x ou mais no cartão.''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço*0.05)
elif opção == 3:
    total = preço
    totparcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${totparcela:.2f}')
elif opção == 4:
    total = preço + (preço * 0.20)
    parcela = int(input('Quantas parcelas? '))
    totparcela = total / parcela
    print(f'Sua compra será parcelada em 2x de R${totparcela:.2f}')
else:
    total = preço
    print('OPÇÃO INVÁLIDA DE PAGAMENTO, TENTE NOVAMENTE!')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')
