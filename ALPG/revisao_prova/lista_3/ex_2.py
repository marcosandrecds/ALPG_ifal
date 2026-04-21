'''
Q2. (1.5 pontos) Controle de Acesso ao Estacionamento
Escreva um programa que gerencia a cancela do estacionamento dos professores.
1) Crie no código uma lista com as placas autorizadas: ["AB-12-CD", "ZX-99-YY", "PT-00-
OK"].
2) Solicite ao usuário que digite a placa do seu veículo.
3) Verifique se a placa digitada está na lista utilizando o operador in.
4) Se a placa estiver autorizada, exiba: ”Acesso concedido. Bem-vindo!”.
5) Caso contrário, exiba: ”Acesso negado. Placa não registrada.”.
'''

print('Controle de Acesso ao Estacionamento')
placas_atorizadas = ["AB-12-CD", "ZX-99-YY", "PT-00-OK"]

placa = str(input('Digite a placa do seu veículo: '))

if placa in placas_atorizadas:
    print('Acesso concedido. Bem-vindo!')
else:
    print('Acesso negado. Placa não registrada.')