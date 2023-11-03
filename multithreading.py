import threading 
import queue
from concurrent.futures import ThreadPoolExecutor
import time

def threading_function(thread_name):
    print(f"Starting thread {thread_name}")
    time.sleep(2)
    print(f"Finishing thread {thread_name}")


def with_thread_pool_executor(amount):
    # Executor will create a pool of threads and manage them, also handles passing in inputs
    with ThreadPoolExecutor(max_workers=amount) as executor:
        executor.map(threading_function, range(amount))

# Doing it with submit instead of map to gain better control over inputs
def thread_pool_executor_submit(amount):
    with ThreadPoolExecutor(max_workers=amount) as executor:
        for i in range(amount):
            executor.submit(threading_function, i)


"""
    Using Locks to prevent race conditions
"""
class DataBase():
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    # Thread name is just for logging purposes
    def locked_update(self, thread_name):
        print(f"{thread_name} is requesting access to the database")
        with self._lock: # sleeps until the lock can be acquired
            print(f"Thread {thread_name} has the lock")
            local_copy = self.value
            local_copy += 1
            time.sleep(1) # Just to make the example work by taking time
            self.value = local_copy
            print(f"Thread {thread_name} releasing lock")
        print(f"Thread {thread_name} released lock")        

def update_database(amount):
    database = DataBase()

    with ThreadPoolExecutor(max_workers=amount) as executor:
        for i in range(amount):
            executor.submit(database.locked_update, i)
    print(database.value)


"""
    Ensuring critical sections of the code run in order using Semaphores
    Semaphores are like locks wherein locks are binary (1 or 0), semaphores can have any integer number of availability.
    Semaphores can be initialised with a default value.
    Doing semaphore.acquire() reduces the semaphore's count by 1
    Doing semaphore.release() increases the count by 1 
"""

class PrintFirstSecondThird():
    """
    Dummy class that calls 3 threads at the same time to show how to ensure they are printed in order
    """
    def __init__(self):
        self.secondLock = threading.Semaphore(0) # Setting to 0 so that the first thread can release it
        self.thirdLock = threading.Semaphore(0)

    def first(self):
        print("First!")
        time.sleep(1)
        self.secondLock.release() # Add 1 to secondLock, then the thread running second can run
    
    def second(self):
        self.secondLock.acquire()
        print("Second!")
        time.sleep(1)
        self.thirdLock.release()
    
    def third(self):
        self.thirdLock.acquire()
        print("Third!")
        time.sleep(1)

def print_in_order():
    printer = PrintFirstSecondThird()
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(printer.second)
        executor.submit(printer.first)
        executor.submit(printer.third)

if __name__ == "__main__":
    # with_thread_pool_executor(3)
    # update_database(5)
    print_in_order()

