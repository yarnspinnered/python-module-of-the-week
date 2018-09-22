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

