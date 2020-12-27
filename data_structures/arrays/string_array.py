arr = 'abcd'
print(arr[1])
# 'b'
print(arr)
# 'abcd'
# Строки неизменяемы:
arr[1] = 'e'
# TypeError:
# "'str' object does not support item assignment"
del arr[1]
# TypeError:
# "'str' object doesn't support item deletion"
# Строки могут быть распакованы в список, в результате чего
# они получают изменяемое представление:
print(list('abcd'))
# ['a', 'b', 'c', 'd']
print(''.join(list('abcd')))
# 'abcd'
# Строки — это рекурсивные структуры данных:
print(type('abc'))
# "<class 'str'>"
print(type('abc'[0]))
# "<class 'str'>"
