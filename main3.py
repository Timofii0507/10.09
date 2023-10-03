try:
    a = float(input('Діагональ a: '))
    b = float(input('Діагональ b: '))
    print('S = ', end='')
    print(0.5*a*b)
except Exception as ex:
    print(ex)