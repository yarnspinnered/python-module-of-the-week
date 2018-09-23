import heapq
import random

l = random.choices(range(5),k=5)
heapq.heapify(l)

#removing items from a heap
while l:
    print(heapq.heappop(l))


#Adding items to a heap
heapq.heappush(l, 1)
heapq.heappush(l, 2)
heapq.heappush(l, 233)

# Get nlargest or nsmallest
print("2 largest: {}".format(heapq.nlargest(2, l)))
print("2 smallest: {}".format(heapq.nsmallest(2, l)))

#heapq merge
l1 = [x for x in range(10)]
l2 = [x for x in range(5,16)]
l3 = [x for x in range(12,20)]
print(list(heapq.merge(l1,l2, l3)))