# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

lst = [1, 1, 2, 3, 4, 5, 5]

res = [x for x in lst if lst.count(x) == 1]

print(res)