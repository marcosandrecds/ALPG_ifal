'''
Q1. (3.0 pontos) Loja de Eletrônicos

Faça um programa que solicite ao usuário o nome de um produto (texto), o valor unitário (nú-
mero real) e a quantidade desejada (número inteiro). O programa deve:

1) Ter uma lista pré-definida no código com os produtos em promoção: ["teclado", "mouse",
"monitor"].
2) Calcular o valor bruto (valor bruto = valor unitário * quantidade).

3) Verificar se o nome do produto digitado pelo usuário está na lista de promoções utili-
zando o operador in.

4) Se o produto estiver na lista, calcular um desconto de 15% sobre o valor bruto. Caso con-
trário, o desconto é zero.

5) Após calcular o primeiro desconto, verificar: se o valor com desconto for maior que R$
200.00 e a quantidade comprada for maior ou igual a 3, aplicar um desconto extra de R$
20.00.
6) Mostrar na tela o valor bruto, o valor total de descontos e o valor líquido a pagar.
'''

print('Loja de Eletônicos')

promocoes = ['teclado', 'mouse', 'monitor']
produto = str(input('Digite o nome do produto: '))
valor = float(input('Digite o valor unitário: '))
quantidade = int(input('Digite a quantidade: '))

valor_bruto = valor * quantidade

if produto in promocoes:
    desconto = valor_bruto * 0.15
else:
    desconto = 0

valor_com_desconto = valor_bruto - desconto

if valor_com_desconto > 200 and quantidade >= 3:
    desconto_extra = 20
else:
    desconto_extra = 0

desconto_total = desconto + desconto_extra
valor_final = valor_bruto - desconto_total

print('Valor bruto:', valor_bruto)
print('Total de descontos:', desconto_total)
print('Valor a pagar:', valor_final)