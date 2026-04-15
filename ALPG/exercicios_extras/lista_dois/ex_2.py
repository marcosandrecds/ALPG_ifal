'''
Q2. Simulador de Crédito Bancário
Um banco decide se concede um empréstimo com base em duas perguntas:
O cliente tem nome limpo? (1-Sim, 2-Não) e Possui renda comprovada? (1-Sim, 2-Não).
O crédito só é aprovado se o nome estiver limpo e houver renda.
Se o nome estiver sujo, exiba "Crédito negado: Restrição no CPF".
Se o nome estiver limpo, mas não houver renda, exiba "Crédito negado: Renda insuficiente".
Dica: Use um if dentro de outro para simular a verificação dupla.
'''

print('Simulador de Crédito Bancário')
nome_limpo = int(input('Você tem o nome limpo?\n1- Sim\n2- Não\n'))
renda = int(input('Você possui renda?\n1- Sim\n2- Não\n'))

if nome_limpo == 1:
    if renda == 1:
        print('Crédito aprovado')
    else:
        print('Crédito negado: Renda insuficiente')
else:
    print('Crédito negado: Restrição no CPF')