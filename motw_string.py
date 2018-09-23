import string

# Capitalize words
original_string = "A cow a dog a duck"
print(original_string)
print(string.capwords(original_string))

# Templates
S = 123
t = string.Template("""
${argType}
foo: ${foo}
bar: ${bar}
                    """
                    )

print(t.substitute(argType="Via function parameters", foo=123, bar= "abc"))
print(t.substitute({"argType":"Via dict", "foo":"123", "bar": "abc"}))

print('=========New style formatting=======')

print("{1} {0}".format(0,1))

# by default, when an object is printed from {}, __format__ is called. Can use !s for __str__ or !r for repr
class Data:
    def __init__(self):
        self.x = "data_x"
        self.y = "data_y"
        self.z = "data_z"

    def __format__(self, format_spec):
        return "format"

    def __str__(self):
        return "str"

    def __repr__(self):
        return "repr"

# Use :_<x for left alignment with length x string and padding with _
d = Data()
print('plain: {0} | with !r: {0!r} | with !s: {0!s}|'.format(d))
print('plain: {0:_>15} | with !r: {0!r:_<15} | with !s: {0!s:15}|'.format(d))

# : denotes formatting specifier. :<paddingcharacter>(<|>)<length to pad to>.<maximum length>
print('plain: {0:_>15} | with !r: {0!r:_<15.2} | with !s: {0!s:15}|'.format(d))

#working with numbers
import math

#Cant really truncate, can only limit precision for floats
print("{:0<10.2f}".format(math.pi))
print("{:0<10d}".format(123456789))

# can name inputs
print("X: {x}".format(y=20,x="x"))

#Can access attributes
print("Data x attribute is {p.x}".format(p=d))