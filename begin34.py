# Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ирисок стоит B рублей. Определить, сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок.

x = float(input())
a = float(input())
y = float(input())
b = float(input())

one_kg_of_candies = a / x
one_kg_of_toffees = b / y
price_difference = one_kg_of_candies / one_kg_of_toffees

print(one_kg_of_candies)
print(one_kg_of_toffees)
print(price_difference)