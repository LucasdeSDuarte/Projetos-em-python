while True:
    print('Digite um numero menor que 0 para parar o programa')
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero*c}')
    print('-' * 30)
print('Volte Sempre!!!')
