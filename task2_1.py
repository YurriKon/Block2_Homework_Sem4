n = int(input('Введите число: '))

res = []
i = 2
while i < n//2 + 1:
    if not n % i:
        res.append(i)
        n //= i
    else:
        i += 1
print(res)