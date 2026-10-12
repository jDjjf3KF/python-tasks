# Даны два целых числа A и B (A < B). Найти сумму квадратов
# всех целых чисел от A до B включительно.

a = int(input())
b = int(input())

sum_of_squares = 0

for i in range(a, b + 1):
    sum_of_squares += i ** 2

print(sum_of_squares)