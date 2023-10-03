try:
    a = float(input('Ширина a: '))
    b = float(input('Висота b: '))
    print('S = ', end='')
    print(a*b)
except Exception as ex:
    print(ex)