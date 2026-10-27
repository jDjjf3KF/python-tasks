# While10. Дано целое число N (> 1). Найти наибольшее целое K,
# при котором выполняется неравенство 3^K < N.

n = int(input())
power = 1
k = 0

while power < n:
    power *= 3
    k += 1

print(k - 1)