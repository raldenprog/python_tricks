import array
arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
print(arr[1])
# 1.5
# Массивы могут изменяться:
arr[1] = 23.0
print(arr)
# array('f', [1.0, 23.0, 2.0, 2.5])
del arr[1]
print(arr)
# array('f', [1.0, 2.0, 2.5])
arr.append(42.0)
print(arr)
# array('f', [1.0, 2.0, 2.5, 42.0])
# Массивы — это "типизированные" структуры данных:
arr[1] = 'привет'
# TypeError: "must be real number, not str"
