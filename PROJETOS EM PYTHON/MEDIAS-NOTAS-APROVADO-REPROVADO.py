n1 = float(input('Qual foi a sua primeira nota: '))
n2 = float(input('Qual foi a segunda nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2 , media))
if 7 > media >= 5:
    print('O aluno esta em RECUPERAÇÂO.')
elif media < 5:
    print('O aluno está REPROVADO.')
elif media >= 7:
    print('O aluno esta APROVADO.')

