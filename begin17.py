# Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму.

A = float(input())
B = float(input())
C = float(input())

AC = abs(C - A)
BC = abs(B - C)
sum_of_segments = abs(sorted([A, B, C][0])) - abs(sorted([A, B, C][-1]))

print(AC)
print(BC)
print(sum_of_segments)