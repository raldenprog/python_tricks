q = []
q.append((2, 'программировать'))
q.append((1, 'есть'))
q.append((3, 'спать'))
# ПРИМЕЧАНИЕ: Не забудьте выполнить пересортировку всякий раз,
# когда добавляется новый элемент, либо используйте
# bisect.insort().
q.sort(reverse=True)
while q:
    next_item = q.pop()
    print(next_item)
# Результат:
# (1, 'есть')
# (2, 'программировать')
# (3, 'спать')
