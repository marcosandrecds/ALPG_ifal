'''
Q5. Verificador de Triângulo Retângulo
Dados três lados de um triângulo (a, b e c), primeiro verifique se eles formam um triângulo (seguindo a regra da Q5 ).
Se formarem, verifique se ele é um Triângulo Retângulo usando o Teorema de Pitágoras (a2=b2+c2).
Nota: Considere para o exercício que o primeiro valor digitado (a) sempre será o maior lado (hipotenusa).
'''

print('Triângulo Retângulo')
a = float(input('Digite o lado a (maior lado): '))
b = float(input('Digite o lado b: '))
c = float(input('Digite o lado c: '))

if a < b + c:
    print('Forma um triângulo.')
    if a**2 == b**2 + c**2:
        print('É um triângulo retângulo.')
    else:
        print('Não é um triângulo retângulo.')
else:
    print('Não forma um triângulo.')