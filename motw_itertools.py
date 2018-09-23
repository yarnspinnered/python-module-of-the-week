from itertools import *

#chain
l1 = [1,2]
l2 = ['a','b']
print(list(chain(l1,l2)))

#chain from iterable
def make_iterables():
    yield [1,2]
    yield['a','b']

print(list(chain.from_iterable(make_iterables())))

#zip different length arrs
l1 = [1]
l2 = ['a','b']
print(list(zip_longest(l1,l2)))

#make multiple copies of an iterator (They depend on the original)
l = range(3)
a,b,c = tee(l,3)
for i in a:
    print('a: ', i)
for i in b:
    print('b: ',i)
#use up original
for i in l:
    print('original ', i)
    if i == 1:
        break
#try using the third
for i in c:
    print('c: ', i)
print("third copy after exhausting original: {}".format(list(c)))

#make a counter
c = count()
for c in range(10):
    print(c)

#repeat
default = repeat("default", 5)
for i in default:
    print(i)

#cycle
c = cycle([1,2,3])
for i in range(5):
    print(c.__next__())

#make a prefix sum
print(list(accumulate([1,2,3])))

#do a groupby. Need to sort by the grouping to make nice subgroupings
l = [1,2,3,4]
l.sort(key= lambda x: x % 2)
for k, g in groupby(l, lambda x : x % 2):
    print(k, list(g))

#take while and drop while
l = [1,2,3,4,5,6]
l_small = takewhile(lambda x : x < 3, l)
l_big = dropwhile(lambda x : x < 3, l)
print(list(l_small))
print(list(l_big))