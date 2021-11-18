# for sem else

PP = ('futebol', 'religião', 'política')
texto = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for t in texto:
    for palavra in t.lower().split():
        if palavra in PP:
            print('Texto possui alguma palavra filtrada:', palavra)
            break
    else:
        print('Texto autorizado:', t)
