from collections import namedtuple

# 2 ways to name the fields of a namedtuple
Person = namedtuple("Person", "name age")
Person = namedtuple("Person", ["name","age"])
Bob = Person("Bob", 23)
print(Bob)
# Two ways to print it
print("{name} is age {age}".format(name=Bob.name, age=Bob.age))
print("{} is age {}".format(*Bob))

