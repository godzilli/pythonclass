from random import randint

ni = -1
ns = randint(0, 9)
# gera um numero aleatorio entre 0 e 9

while ni != ns:
    # diferente, V ou F
    ni = int(input('Informe o número: '))

print('Número secreto {} foi encontrado'.format(ns))
