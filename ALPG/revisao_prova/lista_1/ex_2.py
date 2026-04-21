'''
Q2. (Sistema de RH) Cálculo de Bônus Anual
Uma empresa vai distribuir bônus de fim de ano com base no tempo de casa e na nota de
avaliação do funcionário (de 1 a 5). Escreva um programa que:
1) Solicite o salário atual do funcionário, o seu tempo de empresa (em anos) e a sua nota de
avaliação.
2) Se a nota for igual a 5 e o tempo de casa for maior que 10 anos, o funcionário ganha um
bônus de 20% sobre o salário.
3) Se a nota for igual a 5 ou (a nota for igual a 4 e o tempo de casa for maior que 5 anos),
o bônus será de 10%.
4) Para qualquer outro cenário, o funcionário não tem direito a bônus (0%).
5) Exiba o valor do bônus calculado e o salário total a receber neste mês.
'''

print ('Sistema de RH')

salario = float(input('Digite o seu salário: '))
tempo = int(input('Quanto tempo de empresa? '))
nota = int(input('De 1 a 5, digite sua nota de avaliação: '))

if nota == 5 and tempo > 10:
    aumento = 0.2
elif nota == 5 or (nota == 4 and tempo > 5):
    aumento = 0.1
else:
    aumento = 0

total = salario + salario * aumento

print(f'Você receberá um bônus de {salario * aumento}')
print(f'Seu salário total a receber este mês é de R$ {total}')