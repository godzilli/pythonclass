# for sem else

pp = ('futebol', 'religião', 'política')
texto = [
    'João gosta de futebol e política'
    'A praia foi divertida'
]

for t in texto:
    found = False
    for palavra in t.lower().split():
        if palavra in pp:
            print('Texto possui alguma palavra filtrada:', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado:', t)
