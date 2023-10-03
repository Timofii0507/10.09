try:
    x = float(input('Enter x: '))
    y = float(input('Enter y: '))
    z = float(input('Enter z: '))
    print(x+y+z)
    print(x*y*z)
except Exception as ex:
    print(ex)