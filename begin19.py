# Даны координаты двух противоположных вершин прямоугольника: (x1, y1), (x2, y2). Стороны прямоугольника параллельны осям координат. Найти периметр и площадь данного прямоугольника.

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

perimeter = (abs(x1 - x2) + abs(y1 - y2)) * 2
area = abs(x1 - x2) * abs(y1 - y2)

print(perimeter)
print(area)