from multiprocessing import Queue
q = Queue()
q.put('есть')
q.put('спать')
q.put('программировать')
print(q)
# <multiprocessing.queues.Queue object at 0x1081c12b0>
print(q.get())
# 'есть'
print(q.get())
# 'спать'
print(q.get())
# 'программировать'
print(q.get())
# Блокирует / ожидает бесконечно...
