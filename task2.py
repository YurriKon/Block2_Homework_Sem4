# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]



def factorize(n):
    div = 2
    while div ** 2 <= n:
        if n % div == 0:
            res.append(div)
            n //= div
        else:
            div += 1
    if n != 1:
        res.append(n)

res = []
n = int(input('Введите число: '))
factorize(n)
print(res)