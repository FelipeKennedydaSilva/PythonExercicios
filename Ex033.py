# condições para definir a orddem crescente do menor para o maior

a = int(input('Primeiro número:\n'))
b = int(input('Segundo número:\n'))
c = int(input('Terceiro número:\n'))
# identificando o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# identificando o valor do meio
meio = a
if a>b>c or c>b>a:
    meio = b
if a>c>b or b>c>a:
    meio = c
# identificando o valor menor
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'A ordem crescente do números são: {menor, meio, maior}.')
print(f'O menor valor númerico é {menor}.')
print(f'O maior valor númerico é {maior}.')

