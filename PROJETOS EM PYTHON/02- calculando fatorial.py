from math import factorial
n = int(input('Digite um numero para calcular seu Fatorial: '))
c = n
f = 1
print('Claculando {}! = '. format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c> 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

