# Дано целое число N (> 0). Если оно является степенью числа 3, то вывести TRUE,
# если не является — вывести FALSE.

N = int(input())

rest = N

while rest > 1:
    rest /= 3

print(rest == 1)