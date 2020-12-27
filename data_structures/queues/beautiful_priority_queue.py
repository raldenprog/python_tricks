from queue import PriorityQueue
q = PriorityQueue()
q.put((2, 'программировать'))
q.put((1, 'есть'))
q.put((3, 'спать'))
while not q.empty():
    next_item = q.get()
    print(next_item)
# Результат:
# (1, 'есть')
# (2, 'программировать')
# (3, 'спать')
