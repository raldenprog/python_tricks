arr = 'один', 'два', 'три'
print(arr[0])
'one'
# Кортежи не могут изменяться:
arr[1] = 'привет'
# TypeError:
# "'tuple' object does not support item assignment"
del arr[1]
# TypeError:
# "'tuple' object doesn't support item deletion"
# Кортежи могут содержать произвольные типы данных:
# (При добавлении элементов создается копия кортежа)
print(arr + (23,))
# ('один', 'два', 'три', 23)
