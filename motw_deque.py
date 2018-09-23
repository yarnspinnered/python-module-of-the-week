import time
from collections import deque

#Initialize with some iterable
dq = deque('abcdef')

# Supports len and get item
print(dq[2])
print(len(dq))

# supports remove
dq.remove('b')
print(dq)

#Adding to a deque
dq.appendleft('aa')
dq.append('zz')
print("After appending: {}".format(dq))
dq.extendleft(['aaa', 'aaa'])
dq.extend(['zzz', 'zzz'])
print("After extending: {}".format(dq))

#deques are threadsafe
from threading import Thread
candle = deque(range(10))

def burn(direction, source):
    while True:
        time.sleep(0.1)
        try:
            if direction == "left":
                x = source.popleft()
                source.append(x)
                print("Left burnt. Current state: {}".format(source))
            else:
                source.pop()
                print("Right burnt. Current state: {}".format(source))
        except Exception as e:
            print("Probably ran out of candle: {}".format(e))
            break

left = Thread(target=burn, args=("left", candle))
right = Thread(target=burn, args=("right", candle))
left.start()
right.start()
left.join()
right.join()

#Max size on a queue. Old stuff gets pushed out silently
dq = deque(maxlen=2)
dq.append(1)
dq.append(2)
dq.append(3)
print(dq)
