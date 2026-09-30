# Даны три целых числа. Найти количество положительных
# и количество отрицательных чисел в исходном наборе.

first_number  = int(input())
second_number = int(input())
third_number  = int(input())

print((first_number > 0) + (second_number > 0) + (third_number > 0))
print((first_number < 0) + (second_number < 0) + (third_number < 0))