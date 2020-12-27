s = []
s.append('есть')
s.append('спать')
s.append('программировать')
print(s)
# ['есть', 'спать', 'программировать']
print(s.pop())
# 'программировать'
print(s.pop())
# 'спать'
print(s.pop())
# 'есть'
print(s.pop())
# IndexError: "pop from empty list"
