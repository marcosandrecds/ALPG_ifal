'''
Q4. (2.0 pontos) Classificação de Risco de Saúde
Um posto médico necessita de um programa simples para triagem de pacientes. Escreva um
programa que:
1) Solicite a idade do paciente (inteiro) e o seu peso em kg (real).
2) Solicite se o paciente é fumante (Digite 1 para SIM, 2 para NÃO).
3) Se o paciente tiver mais de 60 anos ou pesar mais de 100 kg, ele é considerado de ”Risco
Moderado”.
4) Verifique a condição anterior. Se ele for de ”Risco Moderado” e também for fumante (opção

1), a sua classificação deve ser atualizada para ”Risco Elevado. Encaminhar para emergên-
cia.”

5) Se não for fumante, mantenha e exiba: ”Paciente de Risco Moderado.”
6) Caso não tenha mais de 60 anos nem mais de 100 kg, exiba: ”Risco Baixo. Aguarde na sala
de espera.”
'''

print('Classificação de Risco de Saúde')

idade = int(input('Digite a sua idade: '))
peso = float(input('Digite seu peso: '))
fumante = int(input('Você é fumante?\n1- Sim\n2- Não\n'))

if idade > 60 or peso > 100:
    if fumante == 1:
        print('Risco Elevado. Encaminhar para emergência.')
    else:
        print('Paciente de Risco Moderado')
else:
    print('Risco Baixo. Aguarde na sala de espera.')