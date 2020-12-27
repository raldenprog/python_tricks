from collections import deque
q = deque()
q.append('есть')
q.append('спать')
q.append('программировать')
print(q)
# deque(['есть', 'спать', 'программировать'])
print(q.popleft())
# 'есть'
print(q.popleft())
# 'спать'
print(q.popleft())
# 'программировать'
print(q.popleft())
# IndexError: "pop from an empty deque"
