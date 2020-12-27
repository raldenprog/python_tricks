from collections import deque
s = deque()
s.append('есть')
s.append('спать')
s.append('программировать')
print(s)
# deque(['есть', 'спать', 'программировать'])
print(s.pop())
# 'программировать'
print(s.pop())
# 'спать'
print(s.pop())
# 'есть'
print(s.pop())
# IndexError: "pop from an empty deque"
