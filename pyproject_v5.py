import math


def circulo(raio):
    print('area do circulo', math.pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = input('informe o raio:')
    circulo(raio)
