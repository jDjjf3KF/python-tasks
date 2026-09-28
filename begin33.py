# Известно, что X кг конфет стоит A рублей. Определить, сколько стоит 1 кг и Y кг этих же конфет.

x = float(input())
a = float(input())
y = float(input())

one_kg_cost = a / x
y_kg_cost = one_kg_cost * y

print(one_kg_cost)
print(y_kg_cost)