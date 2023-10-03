try:
    x = float(input('Зарплата за місяць: '))
    y = float(input('Cума місячного платежу за кредитом у банку: '))
    z = float(input('Заборгованість за комунальні послуги: '))
    print(x-y-z)
except Exception as ex:
    print(ex)