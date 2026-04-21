'''
Q4. (Análise de Crédito) Simulador de Empréstimo
Escreva um programa para avaliar se o banco deve ou não aprovar um empréstimo para o
cliente.
1) Solicite a idade do cliente, a sua renda mensal e o valor do empréstimo desejado.
2) Se o cliente tiver menos de 18 anos, o programa deve exibir ”Empréstimo negado: Cliente
menor de idade.” e encerrar as verificações.
3) Se a idade for válida, calcule o limite máximo de crédito, que é sempre 5 vezes o valor da
renda mensal.

4) Se o valor do empréstimo desejado for maior que o limite máximo calculado, exiba: ”Em-
préstimo negado: Valor excede o limite permitido para sua renda.”

5) Caso contrário, exiba: ”Empréstimo aprovado com sucesso no valor de R$ X” (substituindo X
pelo valor desejado).
'''

print('Análise de Crédito')

idade = int(input('Digite sua idade: '))
renda = float(input('Digite sua renda mensal: '))
emprestimo = float(input('Digite o valor do empréstimo desejado: '))

if idade < 18:
    print('Empréstimo negado: Cliente menor de idade.')
else:
    limite = renda * 5
    
    if emprestimo <= limite:
        print (f'Empréstimo aprovado com sucesso no valor de R$ {emprestimo}')
    else:
        print ('Empréstimo negado: Valor excede o limite permitido para sua renda.')