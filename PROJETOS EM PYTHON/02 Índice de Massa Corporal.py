peso = float(input('Qual e o peso? (Kg) '))
altura = float(input('Qual e a altura? (m) '))
imc = peso / (altura ** 2 )
print('O peso é {}Kg e a altura é {}m'.format(peso, altura))
print('O IMC é {}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 >= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obsidade morbida')