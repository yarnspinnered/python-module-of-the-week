import functools
import time
import timeit


def myfunc(a, b=2):
    "Docstring for myfunc()."
    print('  called myfunc with:', (a, b))


def show_details(name, f, is_partial=False):
    "Show details of a callable object."
    print('{}:'.format(name))
    print('  object:', f)
    if not is_partial:
        print('  __name__:', f.__name__)
    if is_partial:
        print('  func:', f.func)
        print('  args:', f.args)
        print('  keywords:', f.keywords)
    return

#Create partially applied functions
partial_myfunc = functools.partial(myfunc, b=20)
partial_myfunc(2)
# Can override partially applied function but MUST name the overriding arg
partial_myfunc(2,b=3)

#create partially applied methods
def generic_method(self,a, x):
    print(a)
    print(x)

class generic_class:
    def __init__(self):
        self.x = 1
    generic_method = functools.partialmethod(generic_method, "partially applied ")

a = generic_class()
a.generic_method("Look here")
# can cache function input/output pairs. input arguments must be hashable however.
@functools.lru_cache(100)
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

start = time.time()
fib(35)
# can check cache_info and do cache_clear
print(fib.cache_info())
fib.cache_clear()
print(fib.cache_info())
print((time.time() - start))

#functools reduce or foldleft
print(functools.reduce(lambda z,x: z + x, [x for x in range(10)]))