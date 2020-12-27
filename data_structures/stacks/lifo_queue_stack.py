from queue import LifoQueue
s = LifoQueue()
s.put('есть')
s.put('спать')
s.put('программировать')
print(s)
# <queue.LifoQueue object at 0x108298dd8>
print(s.get())
# 'программировать'
print(s.get())
# 'спать'
print(s.get())
# 'есть'
print(s.get_nowait())
# queue.Empty
s.get()
# Блокирует / ожидает бесконечно...
