# Даны переменные A, B, C. Изменить их значения, переместив содержимое A в C, C — в B, B — в A, и вывести новые значения переменных A, B, C.

a = float(input())
b = float(input())
c = float(input())

temp_b = b
temp_c = c

c = a
b = temp_c
a = temp_b

print(a)
print(b)
print(c)