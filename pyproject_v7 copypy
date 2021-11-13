from math import pi
import sys
# import errno


def help(script):
    print("É necessário informar o raio do círculo.\
        Sintaxe: {} <raio>".format(script))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help(sys.argv[0][2:])
        # sys.exit(errno.EPERM)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Area do círculo', area)
