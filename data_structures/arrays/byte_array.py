arr = bytearray((0, 1, 2, 3))
print(arr[1])
# 1
# Байтовые массивы bytearray изменяемы:
arr[1] = 23
print(arr)
# bytearray(b'x00x17x02x03')
print(arr[1])
# 23
# Байтовые массивы bytearray могут расти и сжиматься в размере:
del arr[1]
print(arr)
# bytearray(b'x00x02x03')
arr.append(42)
print(arr)
# bytearray(b'x00x02x03*')
# Байтовые массивы bytearray могут содержать только "байты"
# (целые числа в диапазоне 0 <= x <= 255)
arr[1] = 'привет'
# TypeError: "an integer is required"
arr[1] = 300
# ValueError: "byte must be in range(0, 256)"
# Bytearrays может быть преобразован в байтовые объекты:
# (Это скопирует данные)
print(bytes(arr))
# b'x00x02x03*'
