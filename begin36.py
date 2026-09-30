# Скорость первого автомобиля V1 км/ч, второго — V2 км/ч, расстояние между
# ними S км. Определить расстояние между ними через T часов, если автомобили
# удаляются друг от друга. Данное расстояние равно сумме начального расстояния
# и общего пути, проделанного автомобилями; общий путь = время · суммарная скорость.

velocity_1 = float(input())
velocity_2 = float(input())
distance = float(input())
time = float(input())

distance_after_t_hours = distance + (velocity_1 + velocity_2) * time

print(distance_after_t_hours)