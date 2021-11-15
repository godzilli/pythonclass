a = input("Valor de a:")
b = input("Valor de b:")

if b > a:
    print("b maior que a")
elif a == b:
    print("b e a são iguais")
else:
    print("b é menor que a")

# print("A") if a > b else print("B")

# print("A") if a > b else print("=") if a == b else print("B")

# if a > b and c > a:
    # print("Both conditions are True")

# if a > b or a > c:
    # print("At least one of the conditions is True")

# if b > a:
    # pass faz com que não de erro quando o input não recebe valor
