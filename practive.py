try:
    x = float(input('Enter x: '))
    y = float(input('Enter y: '))
    print(x+y)
    print(x*y)
except Exception as ex:
    print(ex)