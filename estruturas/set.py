PP = {'futebol', 'religião', 'política'}
texto = [
    'João gosta de futebol e política'
    'A praia foi divertida'
]

for t in texto:
    intersecao = PP.intersection(set(t.lower().split()))
    if intersecao:
        print('Texto barrado:', intersecao)
    else:
        print('Permitido.')
