# Скорость лодки в стоячей воде V км/ч, скорость течения реки U км/ч (U < V).
# Время движения лодки по озеру T1 ч, а по реке против течения — T2 ч.
# Определить путь S, пройденный лодкой. Учесть, что при движении против
# течения скорость лодки уменьшается на величину скорости течения.

velocity = float(input())
stream_velocity = float(input())
time_lake = float(input())
time_upstream = float(input())

distance = velocity * time_lake + (velocity - stream_velocity) * time_upstream

print(distance)