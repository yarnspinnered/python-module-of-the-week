import queue
import enum
import threading
from collections import namedtuple

#accessors are put and get

#make a fifo
q = queue.Queue()

#lifo queue
q = queue.LifoQueue()
q.put(1)
q.put(2)
print(q.get())

# priority queue
class Priority(enum.IntEnum):
    LOW = 2
    MID = 1
    HIGH = 0

Job = namedtuple("Job", "priority description")
low_job = Job(Priority.LOW, "not impt")
mid_job = Job(Priority.MID, "somewhat impt")
high_job = Job(Priority.HIGH, "impt")
pq = queue.PriorityQueue()
# Note that we can start workers with an empty queue. This is because get blocks if queue is empty
def process_job():
    while True: # remember to endless loop our workers
        curr = pq.get()
        pq.task_done()
        print(curr)
workers = [threading.Thread(target=process_job), threading.Thread(target=process_job)]
for worker in workers:
    worker.setDaemon(True) # remember to setDaemon or else the process doesnt stop even when main thread is done
    worker.start()


pq.put(low_job)
pq.put(high_job)
pq.put(mid_job)
pq.join() # you can join on a queue
print("main done")