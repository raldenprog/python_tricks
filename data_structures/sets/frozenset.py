vowels = frozenset({'а', 'о', 'э', 'и', 'у', 'ы', 'е', 'е', 'ю',
                    'я'})
vowels.add('р')
# AttributeError:
# "'frozenset' object has no attribute 'add'"

# Множества frozenset хешируемы и могут
# использоваться в качестве ключей словаря:
d = { frozenset({1, 2, 3}): 'привет' }
print(d[frozenset({1, 2, 3})])
# 'привет'
