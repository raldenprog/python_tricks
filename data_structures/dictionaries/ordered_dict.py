import collections
d = collections.OrderedDict(one=1, two=2, three=3)
print(d)
# OrderedDict([('один', 1), ('два', 2), ('три', 3)])
d['четыре'] = 4
print(d)
# OrderedDict([('один', 1), ('два', 2), ('три', 3), ('четыре', 4)])
