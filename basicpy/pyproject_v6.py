def media1(value1, value2, value3):
    return (value1 + value2 + value3) / 3


class mediafinal:
    value1 = float(input('Informe 1° nota:'))
    value2 = float(input('Informe 2° nota:'))
    value3 = float(input('Informe 3° nota:'))
    resultado = media1(value1, value2, value3)
    print('A média é:', resultado)
