casa = float(input('Qual é o valor da casa em reais: R$ '))
salario = float(input('Qual é a sua renda mensal: R$ '))
anos = int(input('Quantas vezes você pretende parcelar: '))
parcelas = casa / (anos * 12)
minimo = salario * 30 / 100
print('O valor da casa é {:.2f}R$, em {} anos'.format(casa, anos))
print('a prestação sera de {:.2f}R$'.format(parcelas))
if parcelas <= minimo:
    print('O Seu financiamento será aprovado!')
else:
    print('A sua renda não permite esse financiamento')
