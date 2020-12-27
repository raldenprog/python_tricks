arr = bytes((0, 1, 2, 3))
print(arr[1])
# 1
# Байтовые литералы имеют свой собственный синтаксис:
print(arr)
# b'x00x01x02x03'
arr = b'x00x01x02x03'
# Разрешены только допустимые "байты":
print(bytes((0, 300)))
# ValueError: "bytes must be in range(0, 256)"
# Байты неизменяемы:
arr[1] = 23
# TypeError:
# "'bytes' object does not support item assignment"
del arr[1]
# TypeError:
# "'bytes' object doesn't support item deletion"
