somaidade = 0
mediaidade = 0
maiorhomem = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):
    print('============ {}ªPESSOA ========',format(p))
    nome = str(input('nome: '))
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: '))
    somaidade += idade
    if  p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorhomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))