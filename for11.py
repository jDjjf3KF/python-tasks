# Дано целое число N (> 0). Найти сумму N2 + (N + 1)2 + (N + 2)2 + ... + (2·N)2.

N = int(input())

sum_ = 0

for i in range(N + 1):
    sum_ += (N + i) ** 2
    print(i, sum_)

print(sum_)