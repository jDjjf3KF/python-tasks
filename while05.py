# Дано целое число N (> 0), являющееся некоторой степенью числа 2: N = 2^K.
# Найти целое число K — показатель этой степени.

N = int(input())

k = 1
power = N

while power != 2:
    power /= 2
    k += 1
    print(power,k)

print(k)