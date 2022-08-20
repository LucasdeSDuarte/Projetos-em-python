total = totmil = menorpreço = cont = 0
barato = ''
print('-'*30)
print('LOJA SUPER BARATÂO')
print('-'*30)
while True:
    nome = str(input('Nome do Produto: '))
    preço = float(input('Preço do Produto [R$]: '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil +=  1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
    terminar = ' '
    while terminar not in 'SN':
        terminar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if terminar == 'N':
       break
print('{:-^40}'.format('Programa encerrado'))
print(f'O total da compra foi {total:2.2f}R$')
print(f'Temos {totmil} custando mais que mil reais')
print(f'O produto mais barato e {barato:} que custa {menorpreço:}')