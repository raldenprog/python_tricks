from queue import Queue
q = Queue()
q.put('есть')
q.put('спать')
q.put('программировать')
print(q)
# <queue.Queue object at 0x1070f5b38>
print(q.get())
# 'есть'
print(q.get())
# 'спать'
print(q.get())
# 'программировать'
print(q.get_nowait())
# queue.Empty
# q.get()
# Блокирует / ожидает бесконечно...
