'''
Q3. Desconto Progressivo em Posto de Combustível
Escreva um algoritmo que leia o tipo de combustível (A-Álcool, G-Gasolina) e a quantidade de litros vendidos.
Calcule o valor a pagar sabendo que:
Álcool: R$ 3,90 por litro. Se vender mais de 20 litros, o preço cai para R$ 3,50 por litro.
Gasolina: R$ 5,50 por litro. Se vender mais de 20 litros, o preço cai para R$ 5,00 por litro.
'''

print('Posto de Combustível')
combustivel = str(input('Qual tipo de combustível?\nA- Álcool\nG- Gasolina\n'))
quantidade = int(input('Quantos litros de combustível?'))

if combustivel == 'A':
    if quantidade <= 20:
        print(f'Você pagará R$ {quantidade * 3.9}')
    else:
        print(f'Você pagará R$ {quantidade * 3.5}')

if combustivel == 'G':
    if quantidade <= 20:
        print(f'Você pagará R$ {quantidade * 5.5}')
    else:
        print(f'Você pagará R$ {quantidade * 5}')