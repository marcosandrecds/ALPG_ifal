'''
Q6. (Segurança) Bloqueio de Múltiplas Tentativas
Um sistema bancário precisa analisar se deve bloquear a conta de um usuário.
1) Solicite ao usuário o número de tentativas de login falhas (inteiro).
2) Solicite se o usuário tentou acessar de um dispositivo não reconhecido (1 para SIM, 2 para
NÃO).
3) Se o número de tentativas for maior ou igual a 3 ou o acesso for de um dispositivo não
reconhecido (opção 1), defina uma variável chamada alerta_seguranca como True. Caso
contrário, defina como False.
4) Crie um if verificando essa variável booleana. Se alerta_seguranca for verdadeira, exiba:
”Conta bloqueada temporariamente por motivos de segurança.”
5) Se for falsa, exiba: ”Acesso liberado. Nenhuma atividade suspeita.”
'''

print('Bloqueio de Múltiplas Tentativas')

tentativas = int(input('Número de tentativas de login falhas: '))
dispositivo = int(input('Tentou acessar de um dispositivo não reconhecido?\n1- Sim\n2- Não\n'))

if tentativas >= 3 or dispositivo == 1:
    alerta_seguranca = True
else:
    alerta_seguranca = False

if alerta_seguranca == True:
    print('Conta bloqueada temporariamente por motivos de segurança.')
else:
    print('Acesso liberado. Nenhuma atividade suspeita.')