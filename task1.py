# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141


from decimal import *

d = int(input('Введите количество знаков после запятой: '))
getcontext().prec = d+1
x = Decimal(355) / Decimal(113)
print(x)