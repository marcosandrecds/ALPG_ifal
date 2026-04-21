'''
Q3. (2.0 pontos) Cinema: Bilheteria Automática
Escreva um programa para validar a compra de ingressos de cinema com base na idade e no
gênero de filme.
1) Tenha uma lista de gêneros restritos no código: ["terror", "guerra", "crime"].
2) Solicite ao usuário o gênero do filme que deseja assistir e a sua idade.
3) Se o gênero escolhido estiver na lista de restritos e a idade for menor que 18 anos, o
programa deve exibir: ”Venda bloqueada: Filme não recomendado para a sua idade.”
4) Se o gênero escolhido estiver na lista, mas a idade for maior ou igual a 18 anos, exiba:
”Venda autorizada. Tenha uma boa sessão.”
5) Se o gênero não estiver na lista, exiba: ”Venda autorizada (Filme de classificação livre).”
'''

print('Bilheteria Automática')

filme = ["terror", "guerra", "crime"]

genero = str(input('Digite o gênero do filme que você quer assistir: '))
idade = int(input('Digite a sua idade: '))

if genero in filme and idade < 18:
    print('Venda bloqueada: Filme não recomendado para a sua idade.')
elif genero in filme and idade >= 18:
    print('Venda autorizada. Tenha uma boa sessão.')
else:
    print('Venda autorizada (Filme de classificação livre).')