def nota_conceito(valor):
    nota = float(valor)

    if nota > 10:
        return 'Nota Inválida'
    elif nota >= 9.1:
        return 'A'
    else:
        return 'Nota Inválida2'


if __name__ == '__main__':
    valor_informado = input('Nota do aluno ')
    conceito = nota_conceito(valor_informado)
    print(conceito)
