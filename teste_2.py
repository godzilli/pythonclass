MLB_team = dict([
    ('Colorado', dict([
        ('Boston', 'Red Sox'),
        ('Minnesota', 'Twins'),
        ('Milwaukee', 'Brewers'),
        ('Seattle', 'Mariners')
    ]))
])

type(MLB_team)
print(type(MLB_team))

if type(MLB_team) == dict:
    print("OK")
