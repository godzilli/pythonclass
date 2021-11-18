from random import randint


def sd():
    return randint(1, 12)


for i in range(1, 13):
    if i % 2 == 1:
        # ímpar
        continue

    if sd() == i:
        print('Par', i)
        break
else:
    print('Ímpar')
