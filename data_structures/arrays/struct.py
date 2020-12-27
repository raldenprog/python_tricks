from struct import Struct
MyStruct = Struct('i?f')
data = MyStruct.pack(23, False, 42.0)
# Вы получаете двоичный объект данных (blob):
print(data)
# b'x17x00x00x00x00x00x00x00x00x00(B'
# BLOB-объекты можно снова распаковать:
print(MyStruct.unpack(data))
# (23, False, 42.0)
