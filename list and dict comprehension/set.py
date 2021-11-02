value = [10, '30', 30, 10, '56']

#  Получение множества с уникальными номерами
value_unique = {int(x) for x in value}
print(value_unique)
