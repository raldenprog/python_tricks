import heapq
q = []
heapq.heappush(q, (2, 'программировать'))
heapq.heappush(q, (1, 'есть'))
heapq.heappush(q, (3, 'спать'))
while q:
    next_item = heapq.heappop(q)
    print(next_item)
# Результат:
# (1, 'есть')
# (2, 'программировать')
# (3, 'спать')
