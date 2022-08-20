print('{:=^40}'.format('LOJAS LUGUIS MODAS'))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTOS
[1] À Vista dinheiro/cheque
[2] À Vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opçao = int(input('Qual é a opção? '))
if opçao == 1:
    total = preco - (preco * 10 / 100)
elif opçao == 2:
    total = preco - (preco * 5 / 100)
elif opçao == 3:
    total = preco
    parcela = total /2
    print('Sua compra sera parcelada em 2x de R${:.f2}'.format(parcela))
elif opçao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('Opção invalida de pagamento tente novamente ')
print('Sua compra de R${:.2f} vai custar {:.2f} no final'.format(preco, total))
