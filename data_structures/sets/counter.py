from collections import Counter
inventory = Counter()
loot = {'клинок': 1, 'хлеб': 3}
inventory.update(loot)
print(inventory)
# Counter({'клинок': 1, 'хлеб': 3})
more_loot = {'клинок': 1, 'яблоко': 1}
inventory.update(more_loot)
print(inventory)
# Counter({'клинок': 2, 'хлеб': 3, 'яблоко': 1})
