import threading
import time
import random
import queue

writeLock = threading.Lock()


class DiningPhilosophers(threading.Thread):
    global writeLock

    def __init__(self, name, left_fork, right_fork, times_to_eat, q):
        super(DiningPhilosophers, self).__init__(name=name)
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.times_to_eat = times_to_eat
        self.times_eated = 0
        self.q = q

    def run(self):
        while True:
            if self.times_eated == self.times_to_eat:
                break
            time.sleep(random.randint(1, 3))
            value = self.pick_up_left_fork()
            try:
                with writeLock:
                    self.q.put(value)
                value = self.pick_up_right_fork()
                try:
                    with writeLock:
                        self.q.put(value)
                        value = self.eat()
                        self.q.put(value)
                    self.times_eated += 1
                finally:
                    value = self.release_right_fork()
                    with writeLock:
                        self.q.put(value)
            finally:
                value = self.release_left_fork()
                with writeLock:
                    self.q.put(value)

    def pick_up_left_fork(self):
        self.left_fork.acquire(timeout=1)
        value = [int(self.name), 1, 1]
        print(value)
        return value
    
    def pick_up_right_fork(self):
        self.right_fork.acquire(timeout=1)
        value = [int(self.name), 2, 1]
        print(value)
        return value

    def eat(self):
        value = [int(self.name), 0, 3]
        print(value)
        return value

    def release_right_fork(self):
        self.right_fork.release()
        value = [int(self.name), 2, 2]
        print(value)
        return value

    def release_left_fork(self):
        self.left_fork.release()
        value = [int(self.name), 1, 2]
        print(value)
        return value

    
    

def init_philosophers(forks, times_to_eat, q):
    philosophers = []

    for idx in range(len(forks)):
        name = idx + 1
        if name != 5:
            p = DiningPhilosophers(
                name, forks[idx], forks[idx+1], times_to_eat, q)
        else:
            p = DiningPhilosophers(name, forks[idx], forks[0], times_to_eat, q)
        philosophers.append(p)
    return philosophers


if __name__ == "__main__":

    forks = [threading.Lock() for i in range(5)]

    n = 1

    q = queue.Queue()

    philosophers = init_philosophers(forks, n, q)

    [p.start() for p in philosophers]

    [p.join() for p in philosophers]

    print(list(q.queue))
