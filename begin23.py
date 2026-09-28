# Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B, B — в C, C — в A, и вывести новые значения переменных A, B, C.

a = float(input())
b = float(input())
c = float(input())

temp_b = b
temp_c = c

b = a
c = temp_b
a = temp_c

print(a)
print(b)
print(c)