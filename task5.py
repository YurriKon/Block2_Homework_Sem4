# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from sympy import poly, Symbol

my_file = open('Многочлен1.txt', 'r')
file_content1 = my_file.read()
print(file_content1)
my_file.close()

my_file2 = open('Многочлен2.txt', 'r')
file_content2 = my_file2.read()
print(file_content2)
my_file2.close()


s1 = file_content1
s1 = s1.replace('^', '**')
s1 = file_content1.split('=')
print(f'Первый многочлен: {s1[0]}')

my_file = open('Многочлен3.txt', 'w')
my_file.write(f'Первый многочлен: {s1[0]}\n')
my_file.close()

s2 = file_content2
s2 = s2.replace('^', '**')
s2 = file_content2.split('=')
print(f'Второй многочлен: {s2[0]}')

my_file = open('Многочлен3.txt', 'a')
my_file.write(f'Второй многочлен: {s2[0]}\n')
my_file.close()

z = poly(s1[0]) + poly(s2[0])
print(f'Сумма многочленов:\n {z}')

my_file = open('Многочлен3.txt', 'a')
my_file.write(f'Сумма многочленов:\n {z}')
my_file.close()
