from collections import defaultdict

def default_value():
    return 'default'

d = defaultdict(default_value)

#Accessing a key that is not available
print(d["not_available_key"])
print(d)

#alternative
normal_d = {}
normal_d.setdefault("not_available key", []).append("default")
print(normal_d)