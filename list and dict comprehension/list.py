"""
3 основных преимущества
1) Простота. List comprehension позволяют избавиться от циклов for, а также делают код более понятным.
2) Скорость. List comprehension быстрее for-циклов, которые он и заменяет.
    Это один из первых пунктов при рефакторинге Python-кода.
3) Принципы функционального программирования. Это не так важно для начинающих,
    но функциональное программирование — это подход, при котором изменяемые данные не меняются.
    Поскольку list comprehensions создают новый список, не меняя существующий, их можно отнести
    к функциональному программированию.
"""

# Простой list comprehension
value = [x for x in range(100)]

# List comprehension с изменением
data = [5, 9, 10]
new_data = [5 * el for el in data]

# List comprehension с if
item = [1, 2, 3, 4, 5]
new_item = [x for x in item if x % 2 == 0]

# List comprehension с вложенным циклом for
matrix = [[x for x in range(1, 4)] for el in range(1, 4)]

# Список дней рождения из списка словарей
people = [{
  "first_name": "Василий",
  "last_name": "Марков",
  "birthday": "9/25/1984"
}, {
  "first_name": "Регина",
  "last_name": "Павленко",
  "birthday": "8/21/1995"
}]

birthdays = [
  person[term]
  for person in people
  for term in person
  if term == "birthday"
]

print(birthdays)

