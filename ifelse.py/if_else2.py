def fe(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 64):
        return 'Adulto'
    else:
        return 'Idade inválida'


if __name__ == '__main__':
    for idade in (17, 20, 87, -2):
        print(f'{idade}: {fe(idade)}')
