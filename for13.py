# Дано целое число N (> 0). Найти значение выражения
# 1.1 − 1.2 + 1.3 − ... (N слагаемых, знаки чередуются).

N = int(input())

expression = 0

for i in range(1, N):
    if i % 2 != 0:
        expression += 1 + i / 10
    else:
        expression -= 1 + i / 10
    print(1 + i / 10, expression)

print(expression)