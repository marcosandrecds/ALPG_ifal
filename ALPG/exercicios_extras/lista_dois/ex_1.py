'''
Q1. Cálculo de IMC (Simplificado)
O Índice de Massa Corporal (IMC) ajuda a avaliar o peso de uma pessoa.
Escreva um programa que leia o peso e a altura, calcule o IMC=peso/(altura∗altura) e classifique o resultado:
Abaixo de 18.5: Abaixo do peso
Até 24.9: Peso normal
Até 29.9: Sobrepeso
30.0 ou mais: Obesidade
Dica: Como no exercício dos nadadores, use a estrutura de elif para testar as faixas de valor em ordem crescente.
'''

print('Cálculo de IMC')
peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura * altura)
print(imc)

if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Peso normal')
elif imc <= 29.9:
    print('Sobrepeso')
else:
    print('Obesidade')