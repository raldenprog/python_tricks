from types import MappingProxyType
writable = {'один': 1, 'два': 2} # доступный для обновления
read_only = MappingProxyType(writable)
# Этот представитель/прокси с доступом только для чтения:
print(read_only['один'])
# 1
read_only['один'] = 23
# TypeError:
# "'mappingproxy' object does not support item assignment"
# Обновления в оригинале отражаются в прокси:
writable['один'] = 42
print(read_only)
# mappingproxy({'один': 42, 'один': 2})