import threading
import logging
import time
from itertools import count

def worker(num):
    logging.debug("This is worker {} printing num {}".format(threading.current_thread(),num))
    time.sleep(1)
    logging.debug("Does this message get out?")

logging.basicConfig(level=logging.DEBUG)

#start and set daemon
threads = []
for i in range(3):
    t = threading.Thread(name=str(i), target=worker,args=(i * 10,))
    threads.append(t)
    t.setDaemon(True)
    t.start()

#can find main_thread and wait for worker threads
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug('joining %s', t.getName())
    t.join()

#alternative way to make workers by subclassing. override run method of our class

class MyThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug("My thread runs with args {} and kwargs {}".format(self.args, self.kwargs))

for i in range(3):
    t = MyThread(args="my args")
    t.start()

# signal between threads with events. Basically multiple threads are waiting for something to be true
# BUT dont care about some underlying resource. use condition in that case
# event.wait([,optional timeout])
# event.is_set()
# event.set()

def wait_for_event(e):
    logging.debug("{} just started waiting".format(threading.current_thread()))
    is_event_set = e.wait()
    logging.debug("Event is set: {}".format(e))

def wait_for_event_non_blocking(e):
    while not e.is_set():
        is_event_set = e.wait(0.5)
        if is_event_set:
            logging.debug("{} Processing event".format(threading.current_thread()))
        else:
            logging.debug("{} doing other processing".format(threading.current_thread()))

e = threading.Event()
t1 = threading.Thread(name="Blocking worker", target=wait_for_event, args=(e,))
t2 = threading.Thread(name="Nonblocking worker", target=wait_for_event_non_blocking, args=(e,))
t1.start()
t2.start()
time.sleep(1.1)
e.set()

# Using locks. Use RLock if the same thread acquires it more than once. Must release once for every acquire
# Locks can be acquired in blocking or nonblocking fashion with a specific timeout
class Counter:
    def __init__(self):
        self.lock = threading.RLock()
        self.c = 0

    def increment(self):
        try:
            self.lock.acquire()
            self.c += 1
        finally:
            self.lock.release()

c = Counter()
def incr_counter(c):
    while c.c < 30:
        time.sleep(0.1)
        c.increment()
        logging.debug("{} Current count after incrementing is: {}".format(threading.current_thread(), c.c))

t1 = threading.Thread(target=incr_counter, args=(c,))
t2 = threading.Thread(target=incr_counter, args=(c,))
t1.start()
t2.start()
t1.join()
t2.join()

#use with to skip acquiring and releasing
class Counter:
    def __init__(self):
        self.lock = threading.RLock()
        self.c = 0

    def increment(self):
        with self.lock:
            self.c += 1
c = Counter()
t1 = threading.Thread(target=incr_counter, args=(c,))
t2 = threading.Thread(target=incr_counter, args=(c,))
t1.start()
t2.start()
t1.join()
t2.join()

# Synchronizing access to a resource that eventually becomes available
def consumer(cond):
    logging.debug("Waiting for condition")
    with cond:
        cond.wait()
        logging.debug("resource is available")

def producer(cond):
    with cond:
        logging.debug("making resource available")
        cond.notifyAll()

condition = threading.Condition()
t1 = threading.Thread(name="consumer", target=consumer, args=(condition,))
t2 = threading.Thread(name="producer", target=producer, args=(condition,))
t1.start()
t2.start()
t1.join()
t2.join()

# limit number of workers using a resource

class ActivePool:
    def __init__(self):
        self.active = []
        self.lock = threading.Lock()

    def make_active(self, name):
        self.active.append(name)
        logging.debug("After adding. Running: %s",self.active)

    def make_inactive(self, name):
        self.active.remove(name)
        logging.debug("After removal, running: %s", self.active)

def worker(s, pool):
    logging.debug("waiting to join pool")
    with s:
        name = threading.current_thread().getName()
        pool.make_active(name)
        time.sleep(0.1)
        pool.make_inactive(name)

pool = ActivePool()
semaphore = threading.Semaphore(2)
for i in range(5):
    t = threading.Thread(
        name="Worker {}".format(i),
        target=worker,
        args=(semaphore, pool)
    )
    t.start()