'''
Q4. Conversor de Notas para Conceito
Em algumas faculdades, as notas são convertidas em conceitos. Faça um programa que leia uma nota (0 a 10) e exiba o conceito:
9.0 a 10.0: Conceito A
7.5 a 8.9: Conceito B
6.0 a 7.4: Conceito C
Abaixo de 6.0: Conceito D
Nota: Se a nota for maior que 10 ou menor que 0, informe "Nota inválida".
'''

print('Conversor de Notas para Conceito')
nota = float(input('Digite a nota: '))

if nota > 10 or nota < 0:
    print('Nota inválida.')
elif nota < 6:
    print('Conceito D')
elif nota <= 7.4:
    print('Conceito C')
elif nota <= 8.9:
    print('Conceito B')
else:
     print('Conceito A')