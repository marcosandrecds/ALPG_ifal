'''
Q2. (4.0 pontos) Sistema de Empréstimos da Biblioteca
Uma biblioteca deseja um programa para registrar o empréstimo de livros. Conforme as regras
da biblioteca, elabore um programa que:
1) Possua uma lista de livros restritos no código: ["1984", "duna", "fundacao"].
2) Solicite ao usuário o nome do livro que ele deseja pegar emprestado.
3) Solicite a quantidade de dias que o usuário pretende ficar com o livro.
4) Se o livro solicitado estiver na lista de restritos ou a quantidade de dias solicitada for
maior do que 14, o programa deve exibir a mensagem: ”Empréstimo negado: Livro restrito
ou prazo excede o limite permitido.” e encerrar a verificação.
5) Caso contrário (se não for restrito e o prazo for aceitável), o programa deve perguntar ao
usuário: ”Você possui multas pendentes na biblioteca? (sim/nao)”.

6) Se a resposta for igual a ”sim”, exibir: ”Empréstimo bloqueado devido a pendências financei-
ras.”

7) Mas, se a resposta for igual a ”nao”, exibir: ”Empréstimo aprovado! Devolva em X dias.” (onde
X é o número de dias que o usuário digitou no passo 3).
'''

print('Sistema de Empréstimos da Biblioteca')

lista_de_livros = ["1984", "duna", "fundacao"]
livro = str(input('Nome do livro que deseja pegar emprestado: '))
dias = int(input('Quantidade de dias que pretende ficar com o livro: '))

if livro in lista_de_livros or dias > 14:
    print('Empréstimo negado: Livro restrito ou prazo excede o limite permitido.')
else:
    pendencias = int(input('Você possui multas pendentes na biblioteca?\n1- Sim\n2- Não\n'))
    if pendencias == 1:
        print('Empréstimo bloqueado devido a pendências financeiras.')
    else:
        print (f'Empréstimo aprovado! Devolva em {dias} dias.')