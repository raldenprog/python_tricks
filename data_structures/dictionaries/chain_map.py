from collections import ChainMap
dict1 = {'один': 1, 'два': 2}
dict2 = {'три': 3, 'четыре': 4}
chain = ChainMap(dict1, dict2)
print(chain)
# ChainMap({'один': 1, 'два': 2}, {'три': 3, 'четыре': 4})

# ChainMap выполняет поиск в каждой коллекции в цепочке
# слева направо, пока не найдет ключ (или не потерпит неудачу):
print(chain['три'])
#  3
print(chain['один'])
#  1
print(chain['отсутствует'])
# KeyError: 'отсутствует'
