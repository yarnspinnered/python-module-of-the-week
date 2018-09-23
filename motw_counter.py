from collections import Counter

# 3 ways to make a counter
print(Counter(['a','b','b','c','c','c']))
print(Counter({'a':1,'b':2,'c':3}))
print(Counter(a=1, b=2, c=3))

# Adding another collection to a counter. Can update with another iterable or some counter/dictionary
original = Counter(['a','b','b','c','c','c'])
original.update(['a','b','b','c','c','c'])
original.update(original)
print(original)

#Access count of a specific element
print(original['c'])
# Get all elements in counter
print(list(original.elements()))

# Get most common
print(original.most_common(2))

#Arithmetic oeprations
abc_counter = Counter('abc')
ccd_counter = Counter('ccd')
print("abc + ccd is {}".format(abc_counter + ccd_counter))
print("abc - ccd is {}".format(abc_counter - ccd_counter))
print("abc & ccd is {}".format(abc_counter & ccd_counter))
print("abc | ccd is {}".format(abc_counter | ccd_counter))