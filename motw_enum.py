from enum import Enum, IntEnum

class LogLevel(Enum):
    LOW = 0
    MID = 1
    HIGH = 2

#check out log levels. Has a name and value pair
print(LogLevel.LOW.name)
print(LogLevel.LOW.value)

for log_level in LogLevel:
    print(log_level)

# Comparing enum instances
print(LogLevel.LOW is LogLevel.LOW)
print(LogLevel.LOW == LogLevel.LOW)
try:
    print(sorted(LogLevel))
except Exception as e:
    print("This is the error we get when trying to sort a unordered Enum: {}".format(e))

# Getting a ordering for enum
class OrderedLogLevel(IntEnum):
    LOW = 0
    MID = 1
    HIGH = 2

    ALIAS_LOW = 0

print("Sorted IntEnum: {}".format(sorted(OrderedLogLevel)))
print("LOW IS ALIAS_LOW: {}".format(OrderedLogLevel.ALIAS_LOW is OrderedLogLevel.LOW))