#maintain a sorted list in sorted order while mutating it
import bisect

#adding values by finding position then inserting. Or just shortcut insort
l = [x for x in range(10)]
l.insert(bisect.bisect_left(l,2.5), 2.5)
bisect.insort_left(l, 3.5)
print(l)
