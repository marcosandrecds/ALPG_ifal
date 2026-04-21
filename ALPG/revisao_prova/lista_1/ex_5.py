'''
Q5. (Game Logic) Sistema de Criação de Itens (Crafting)

Em um jogo de RPG, o jogador quer criar uma ”Poção de Cura”. Para isso, ele precisa de ingre-
dientes específicos.

1) Crie uma lista representando o inventário do jogador: ["espada", "frasco_vazio", "mapa",
"flor_de_fogo", "moedas"].
2) Verifique se o item "frasco_vazio" está na lista de inventário e se o item "flor_de_fogo"
também está na lista.
3) Se ele possuir ambos os itens (utilize o operador in e and), exiba: ”Você criou uma Poção de
Cura com sucesso!”
4) Se faltar qualquer um dos dois itens, exiba: ”Materiais insuficientes. Você precisa de um
frasco vazio e de uma flor de fogo.”
5) Verifique isoladamente: se o item "poeira_magica" não estiver no inventário (not in),
avise o jogador: ”Dica: Você não possui Poeira Mágica para poções avançadas.”
'''

print('Sistema de Criação de Itens')
print('Você quer criar um poção de cura.\nVerificando se os itens frasco vazio e flor de fogo estão em seu inventário.')
inventario = ["espada", 'frasco_vazio', 'flor_de_fogo', "mapa", "moedas"]

if 'frasco_vazio' in inventario and 'flor_de_fogo' in inventario:
    print('Você criou uma Poção de Cura com sucesso!')
else:
    print('Materiais insuficientes. Você precisa de um frasco vazio e de uma flor de fogo.')

if "poeira_magica" not in inventario:
    print('Dica: Você não possui Poeira Mágica para poções avançadas.')