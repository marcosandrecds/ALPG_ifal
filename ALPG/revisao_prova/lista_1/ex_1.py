'''
Q1. (Sistema de E-commerce) Cálculo de Frete
Escreva um programa que calcule o valor final de uma compra online, aplicando regras de frete
grátis por região.
1) Crie no código uma lista com as siglas dos estados da região Sudeste: ["SP", "RJ", "MG",
"ES"].
2) Solicite ao usuário o valor total dos produtos no carrinho (número real).
3) Solicite a sigla do estado para entrega.
4) Se a sigla digitada estiver na lista e o valor da compra for maior que R$ 150,00, o frete é
grátis (R$ 0,00).
5) Se a sigla estiver na lista, mas a compra for menor ou igual a R$ 150,00, o frete custará R$
15,00.
6) Se a sigla não estiver na lista, o frete fixo é de R$ 35,00, independentemente do valor da
compra.
7) Exiba o valor do frete e o valor total final (produtos + frete) a ser pago.
'''

print('Sistema de e-commerce')

estados = ['SP', 'RJ', 'MG', 'ES']

valor = float(input('Valor total dos produtos no carrinho: '))
frete = str(input('Digite a sigla do estado para entrega: '))

if valor > 150 and frete in estados:
    v_frete = 0
elif valor <= 150 and frete in estados:
    v_frete = 15
else:
    v_frete = 35

total = valor + v_frete

print(f'Valor dos produtos R$ {valor}')
print(f'Valor do frete R$ {v_frete}')
print(f'Valor total a pagar R$ {total}')