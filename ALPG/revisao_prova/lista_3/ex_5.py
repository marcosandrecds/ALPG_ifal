'''
Q5. (1.5 pontos) Simulador de Descontos VIP
Escreva um programa para uma loja calcular descontos cumulativos.
1) Solicite o valor total das compras do cliente.
2) Pergunte se o cliente possui o cartão VIP da loja (Digite ”sim” ou ”nao”).

3) Se o valor da compra for maior que R$ 500,00 e o cliente for VIP (”sim”), aplique um des-
conto de 20%.

4) Se o valor for maior que R$ 500,00 ou o cliente for VIP (mas não ambos simultaneamente),
aplique um desconto de 10%.
5) Se nenhuma das condições anteriores for verdade, o desconto é de 0%.
6) Exiba o valor do desconto e o montante final a pagar.
'''

print('Simulador de Descontos VIP')

total = float(input('Valor total das compras: '))
vip = str(input('Você possui o cartão VIP da loja (Digite sim ou nao).'))

if total > 500 and vip == 'sim':
    desconto = total * 0.2
elif total > 500 or vip == 'sim':
    desconto = total * 0.1
else:
    desconto = 0

valor = total - desconto

print(f'O desconto é R$ {desconto}\nO valor total é {valor}')