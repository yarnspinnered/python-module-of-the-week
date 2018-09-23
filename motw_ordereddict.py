import string
from collections import OrderedDict

# unordreed iteration vs ordered iteration
d = {}
d['angery'] = 235
d['bull'] = 333
d['fishing'] = 954

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
for k,v in d.items():
    print("unordered: {} {}".format(k,v))

for k,v in od.items():
    print("ordered: {} {}".format(k,v))

#Equality in ordereddict. Factors in order as well unlike regular dicts
d = {}
d['a'] = 1
d['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print("What if same contents and different order in regular dict? == is {}".format(d==d2))
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1
print("What if same contents and different order in ordereddict? == is {}".format(d==d2))

print("Original dict: {}".format(od))
od.move_to_end('a', True)
print("after move to end {}".format(od))
