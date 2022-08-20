from datetime import date
atual = date.today().year
nasc = int(input('Em qual você nasceu: '))
print('Qual é o seu sexo:\n[1] Masculino\n[2] Feminino ')
sex = int(input('Escolha entra a opção 1 ou 2: '))
idade = atual - nasc
if sex == 1:
    print('Você podera se alistar')
else:
    print('Mulheres não podem se alistar')
    exit()
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:#poderia encerrar com else por não tem mais opçoes
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))

